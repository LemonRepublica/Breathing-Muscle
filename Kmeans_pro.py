# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 02:29:00 2019

@author: 10536
"""

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import cv2

def Kmeans_pro(img,clu):
    img = np.transpose(img)
    m = img.shape[0]
    n = img.shape[1]
    data = []
    for i in range(m):
        for j in range(n):
            data.append(img[i,j])

    img_r = np.mat(data).reshape(-1,1)
    label = KMeans(n_clusters=clu).fit_predict(img_r)  #聚类，获得每个像素的类别（有5类）
    label = label.reshape([m,n]) 
    label = np.transpose(label)
    return label

