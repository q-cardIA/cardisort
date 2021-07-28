# cardisort
CardiSort: a convolutional neural network for cross vendor automated sorting of cardiac MR images

This is a deep learning network which was developed to sort cardiac MRI images by sequence type and imaging plane, facilitating efficient and fully automated post-processing pipelines.

Please find the pre-trained model weights [here](https://emckclac-my.sharepoint.com/:u:/g/personal/k1633520_kcl_ac_uk/EZ-7bZsMOCxEuCrCsoa7o2sBpBSJvuaHn9mIsgktnbvjvA?e=gCgzdh).

The model can be run to sort a folder or DICOM images as:

    >> python cardisort_inference.py [INPUT_FOLDER] or  python cardisort_inference.py [INPUT_FOLDER] [OUTPUT_FOLDER]
