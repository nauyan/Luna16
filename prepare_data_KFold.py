import glob
import cv2
import numpy as np
import png
import os
import progressbar

from sklearn.model_selection import KFold

working_path = "./dataset/volumes_modified/"
train_img = np.load("dataset/volumes_modified/trainImages.npy")
train_mask = np.load("dataset/volumes_modified/trainMasks.npy")
print(train_img.shape,train_mask.shape)

test_img = np.load("dataset/volumes_modified/testImages.npy")
test_mask = np.load("dataset/volumes_modified/testMasks.npy")
print(test_img.shape,test_mask.shape)

X = np.vstack((train_img,test_img))
Y = np.vstack((train_mask,test_mask))
print(X.shape,Y.shape)

kfold = KFold(5, True, 1)
# enumerate splits
count = 1
for train, test in kfold.split(X,Y):
	#print('train: %s, test: %s' % (data[train].shape, data[test].shape))
    print(X[train].shape,Y[train].shape,X[test].shape,Y[test].shape)
    np.save(working_path+"trainImages_"+str(count)+".npy", X[train])
    np.save(working_path+"trainMasks_"+str(count)+".npy", Y[train])
    np.save(working_path+"testImages_"+str(count)+".npy", X[test])
    np.save(working_path+"testMasks_"+str(count)+".npy", Y[test])
    count = count + 1