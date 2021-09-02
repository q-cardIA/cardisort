# cardisort
CardiSort: a convolutional neural network for cross vendor automated sorting of cardiac MR images

This is a deep learning network which was developed to sort cardiac MRI images by sequence type and imaging plane, facilitating efficient and fully automated post-processing pipelines.

Please find the pre-trained model weights [here](https://emckclac-my.sharepoint.com/:u:/g/personal/k1633520_kcl_ac_uk/EZ-7bZsMOCxEuCrCsoa7o2sBpBSJvuaHn9mIsgktnbvjvA?e=gCgzdh).

The model can be run to sort a folder of DICOM images as:

    >> python cardisort_inference.py [INPUT_FOLDER] 
or    

    >> python cardisort_inference.py [INPUT_FOLDER] [OUTPUT_FOLDER]
This assumes that the input folder contains only one CMR study from one patient.


If you find this code helpful in your research please cite the following paper:
```
@article{lim2021cardisort,
  title={CardiSort: a convolutional neural network for cross vendor automated sorting of cardiac MR images},
  author={Lim, Ruth P, and Kachel, Stefan, and Villa, Adriana DM, and Kearney, Leighton, and Bettencourt, Nuno, and Young, Alistair A, and Chiribiri, Amedeo,  and Scannell, Cian M},
  year={under review}
}
```
