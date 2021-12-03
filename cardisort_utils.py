import os 
import numpy as np
import pydicom
import cv2

def write_sorted(list_of_files, out_fold, seq, plane, series_no):

    # this_seq_fold_series = os.path.join(out_fold, f"{seq}_{plane}", f"series{int(series_no)}")
    this_seq_fold_series = os.path.join(out_fold, f"{seq}_{plane}", str(list_of_files[0].SeriesDescription))

    if not os.path.exists(this_seq_fold_series):
        os.makedirs(this_seq_fold_series)
    for ii,file in enumerate(list_of_files):
        num = f"0000{ii}"
        file.save_as(os.path.join(this_seq_fold_series, f"{num[-4:]}.dcm"))

def get_files(the_dir):

    all_files = []
    all_patient_items = os.listdir(the_dir)
    all_patient_items = [os.path.join(the_dir, p) for p in all_patient_items]
    for itm in all_patient_items:
        if os.path.isfile(itm):
                all_files.append(itm)
        if os.path.isdir(itm):
            series_dir_files = os.listdir(itm)
            series_dir_files = [os.path.join(itm,x) for x in series_dir_files]
            for sub_itm in series_dir_files:
                if os.path.isfile(sub_itm):
                    all_files.append(sub_itm)

    MRI_images = []
    for file in all_files:
        try:
            if pydicom.dcmread(file).SOPClassUID == '1.2.840.10008.5.1.4.1.1.4':
                MRI_images.append(file)
        except Exception:
            pass

    return MRI_images
    
def get_inference_dict(patient_dict, M, N):
    inference_dict = {}
    secondary_files = []
    for key, this_series in patient_dict.items():
        if 'secondary' not in this_series[0].SeriesDescription.lower():
            
            this_series_ims = selected_images(this_series)
            im1 = this_series_ims[0].pixel_array
            im1 = cv2.resize(im1, dsize=(M, N), interpolation=cv2.INTER_LINEAR)
            if len(this_series_ims) == 1:
                im2 = im1.copy()
                im3 = im1.copy()
            else:
                im2 = this_series_ims[1].pixel_array
                im2 = cv2.resize(im2, dsize=(M, N), interpolation=cv2.INTER_LINEAR)
                if len(this_series_ims) == 2:
                    im3 = im1.copy()
                else:
                    im3 = this_series_ims[2].pixel_array
                    im3 = cv2.resize(im3, dsize=(M, N), interpolation=cv2.INTER_LINEAR) 

            normim1 =  ( im1 - np.min(im1) ) / ( np.max(im1) - np.amin(im1) + 1e-6 ).astype('float32')
            normim2 =  ( im2 - np.min(im2) ) / ( np.max(im2) - np.amin(im2) + 1e-6 ).astype('float32')
            normim3 =  ( im3 - np.min(im3) ) / ( np.max(im3) - np.amin(im3) + 1e-6 ).astype('float32')
            normalised_newim = np.stack((normim1, normim2, normim3), axis=-1)
            inference_dict[key] = normalised_newim 

    return inference_dict


def get_philips_ge_dict(files):

    this_patient_dict = {}
    instance_nums = {}
    for file in files:
        dicom_ds = pydicom.read_file(file)
        this_patient_dict.setdefault(dicom_ds.SeriesInstanceUID, []).append(dicom_ds)
        instance_nums.setdefault(dicom_ds.SeriesInstanceUID, []).append(int(dicom_ds.InstanceNumber))

    return arrange_by_instance_philips_ge(this_patient_dict, instance_nums)

def arrange_by_instance_philips_ge(patient_dict, all_instances):

    ordered_patient_dict = {}
    for key, ims in patient_dict.items():
        the_instance_nums = all_instances[key]
        the_order = np.argsort(the_instance_nums)
        new_ims = []
        for ii in the_order:
            new_ims.append(ims[ii])
        ordered_patient_dict[key] = new_ims
    return ordered_patient_dict

def get_siemens_dict(files):

    this_patient_dict = {}
    info_for_order = {}
    for file in files:
        dicom_ds = pydicom.read_file(file)
        this_patient_dict.setdefault(dicom_ds.ProtocolName, []).append(dicom_ds)
        info_for_order.setdefault(dicom_ds.ProtocolName, []).append([float(dicom_ds.SeriesTime),dicom_ds.SeriesInstanceUID,int(dicom_ds.InstanceNumber)])

    return arrange_by_instance_siemens(this_patient_dict,info_for_order)

def arrange_by_instance_siemens(patient_dict, instance_nums):

    ordered_patient_dict = {}
    for key, ims in patient_dict.items():
        instances = instance_nums[key]
        the_order = sorted(range(len(instances)), key=lambda k: instances[k]) 
        new_ims = []
        for ii in the_order:
            new_ims.append(ims[ii])
        ordered_patient_dict[key] = new_ims
    return ordered_patient_dict


def selected_images(input_list):
    # if our list is empty return nan, have to see whether this works in our case
    if 0 == len(input_list):
        return np.nan
    # if our list has just two elements we want to avoid to use the first one
    if 0 < len(input_list) < 4:
        return input_list
    # get the index of the middle
    middle = (len(input_list)//2)
    return input_list[0], input_list[middle], input_list[-1]