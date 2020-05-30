import glob
import cv2
import numpy as np
import png
import os
import progressbar

train_img = np.load("dataset/volumes_modified/trainImages.npy")
train_mask = np.load("dataset/volumes_modified/trainMasks.npy")

count = 0
for img, mask in progressbar.progressbar(zip(train_img,train_mask)):
    img = img.reshape(512,512)
    img = cv2.normalize(img,img,alpha=0,beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    
    mask = mask.reshape(512,512)
    mask = cv2.normalize(mask,mask,alpha=0,beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    mask[mask>0]=1
    
    cv2.imwrite("dataset/prepared_data/train/images/"+str(count)+".png",img)
    cv2.imwrite("dataset/prepared_data/train/masks/"+str(count)+".png",mask)
    count = count + 1


test_img = np.load("dataset/volumes_modified/testImages.npy")
test_mask = np.load("dataset/volumes_modified/testMasks.npy")

count = 0
for img, mask in progressbar.progressbar(zip(test_img,test_mask)):
    img = img.reshape(512,512)
    img = cv2.normalize(img,img,alpha=0,beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    
    mask = mask.reshape(512,512)
    mask = cv2.normalize(mask,mask,alpha=0,beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    mask[mask>0]=1
    
    cv2.imwrite("dataset/prepared_data/test/images/"+str(count)+".png",img)
    cv2.imwrite("dataset/prepared_data/test/masks/"+str(count)+".png",mask)
    count = count + 1
