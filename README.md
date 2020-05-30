## Repository for [LUNA (LUng Nodule Analysis) 2016](https://luna16.grand-challenge.org/Home/).

<p align="center">Note: If you're interested in using it, feel free to ⭐️ the repo so we know!</p>


## Dataset
Lung cancer is the leading cause of cancer-related death worldwide. Screening high risk individuals for lung cancer with low-dose CT scans is now being implemented in the United States and other countries are expected to follow soon. In CT lung cancer screening, many millions of CT scans will have to be analyzed, which is an enormous burden for radiologists. Therefore there is a lot of interest to develop computer algorithms to optimize screening. 

A vital first step in the analysis of lung cancer screening CT scans is the detection of pulmonary nodules, which may or may not represent early stage lung cancer. Many Computer-Aided Detection (CAD) systems have already been proposed for this task. The LUNA16 challenge will focus on a large-scale evaluation of automatic nodule detection algorithms on the LIDC/IDRI data set.

Further details about datase can be seen on the dataset [page](https://luna16.grand-challenge.org/Data/)

To download the dataset follow these steps:
```
mkdir dataset/
mkdir dataset/volumes
mkdir dataset/volumes/images/
mkdir dataset/volumes/masks/
mkdir dataset/volumes_modified/
mkdir dataset/volumes_modified/images/
mkdir dataset/volumes_modified/masks/
cp download.sh dataset/volumes/
cp extract.sh dataset/volumes/
./dataset/volumes/download.sh
./dataset/volumes/extract.sh
```

## Installation 
Installation can be done using the commands below:
```
pip install src/Mask_RCNN/requirements.txt
python src/Mask_RCNN/setup.py install
pip install requirements.txt
```

## Trained Weights
Trained weights can be dowloaded from Google Drive [Link](https://drive.google.com/drive/folders/1h8nu07VJ_AxVdplNk8sQdjw1SssJOuJx?usp=sharing). After you have donwloaded the weights do the follwing:
```
mkdir logs/
```
After creating logs directory copy the Luna.zip file downloaded from google drive into the folder and extract it.

## Training 
Training can be started using Luna.py file. To start training use the following command:
```
python Luna.py train --dataset=dataset/prepared_data --weights=imagenet --logs logs/
```
Luna.py file contains hyper-parameters of training and testing update them according to your needs.

## Inference
Inference can be done using Luna_Inference.ipynb file.

If there are any problems feel free to open an issue.

## Author
`Maintainer` [Syed Nauyan Rashid](https://https://github.com/nauyan) (nauyan@hotmail.com)
