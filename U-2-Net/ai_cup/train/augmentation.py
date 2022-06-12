# -*- coding: utf-8 -*-
"""
Created on Sat May 28 22:22:04 2022

@author: Chi
"""



import cv2
from matplotlib import pyplot as plt 
import albumentations as A
import os
   
transform = A.HorizontalFlip(p=1)

images = os.listdir(path = ".\image")
print(len(images))
masks = os.listdir(path = ".\mask")
print(len(masks))
print(os.getcwd())

os.chdir(".\image")
print(os.getcwd())




i = 1053
for image in images:
   img = cv2.imread(image)   
   img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   transformed = transform(image = img)     
   filename = 'train_' + str(i) + '.jpg'
   i = i+1
   cv2.imwrite(filename, transformed["image"])
j = 1053
os.chdir(".\mask")
print(os.getcwd())
for mask in masks:
    msk = cv2.imread(mask)
    cv2.cvtColor(msk, cv2.COLOR_BGR2RGB)
    transformed = transform(image = msk)
    filename = 'train_' + str(j) + '.jpg'
    j = j+1
    cv2.imwrite(filename, transformed["image"])
    


