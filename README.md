# cardisort
CardiSort: a convolutional neural network for cross vendor automated sorting of cardiac MR images

This is a deep learning network which was developed to sort cardiac MRI images by sequence type and imaging plane, facilitating efficient and fully automated post-processing pipelines.

Please find the pre-trained model weights [here](https://emckclac-my.sharepoint.com/:u:/g/personal/k1633520_kcl_ac_uk/EZ-7bZsMOCxEuCrCsoa7o2sBpBSJvuaHn9mIsgktnbvjvA?e=gCgzdh).

The model can be run to sort a folder of DICOM images as:

    >> python cardisort_inference.py [INPUT_FOLDER] 
or    

    >> python cardisort_inference.py [INPUT_FOLDER] [OUTPUT_FOLDER]
**This assumes that the input folder contains only one CMR study from one patient.** For an idea of how to run on multiple input folders from multiple patients see `run_multiple.sh`.


If you find this code helpful in your research please cite the following [paper](https://arxiv.org/abs/2109.08479):

Ruth P Lim, Stefan Kachel, Adriana DM Villa, Leighton Kearney, Nuno Bettencourt, Alistair A Young, Amedeo Chiribiri, and Cian M Scannell. CardiSort: a convolutional neural network for cross vendor automated sorting of cardiac MR images. arXiv preprint
arXiv:2109.08479, 2021.

```
@misc{lim2021cardisort,
      title={CardiSort: a convolutional neural network for cross vendor automated sorting of cardiac MR images}, 
      author={Ruth P Lim and Stefan Kachel and Adriana DM Villa and Leighton Kearney and Nuno Bettencourt and Alistair A Young and Amedeo Chiribiri and Cian M Scannell},
      year={2021},
      eprint={2109.08479},
      archivePrefix={arXiv},
      primaryClass={eess.IV}
}
```
