# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 04:47:08 2019

@author: 10536
"""
import get_file
import cv2
import numpy as np

for file in get_file.getFiles(r"C:\Users\10536\Desktop\MSc_Project\py\Unet\deform\train\label", '.jpg'):
    path = file[0]
    print(path)
    file_name = file[1]
    print(file_name)
    f = cv2.imread(r"%s.jpg"%(path))
    for i in range(f.shape[0]):
        for j in range(f.shape[1]):
            for k in range(f.shape[2]):
                if f[i,j,k] > 220:
                    f[i,j,k] = 255
                else:
                    f[i,j,k] = 0
    path2 = path.rstrip("_mask")
    cv2.imwrite(r"%s.jpg"%(path2), f)
    print("done")
    
