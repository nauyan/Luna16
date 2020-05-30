## Repository for [LUNA (LUng Nodule Analysis) 2016](https://ieeexplore.ieee.org/document/8880654).

<p align="center">Note: If you're interested in using it, feel free to ⭐️ the repo so we know!</p>


## Dataset
In total, 888 CT scans are included. The LIDC/IDRI database also contains annotations which were collected during a two-phase annotation process using 4 experienced radiologists. Each radiologist marked lesions they identified as non-nodule, nodule < 3 mm, and nodules >= 3 mm. See this publication for the details of the annotation process. The reference standard of our challenge consists of all nodules >= 3 mm accepted by at least 3 out of 4 radiologists. Annotations that are not included in the reference standard (non-nodules, nodules < 3 mm, and nodules annotated by only 1 or 2 radiologists) are referred as irrelevant findings. The list of irrelevant findings is provided inside the evaluation script (annotations_excluded.csv).

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
