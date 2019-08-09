# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 02:29:00 2019

@author: 10536
"""

import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def loadData(filePath):
    f = open(filePath,'rb')
    data = []
    img = image.open(f)   #打开图像
    m,n = img.size        #获取图像尺寸
    for i in range(m):
        for j in range(n):
            x,y,z = img.getpixel((i,j))   #得到图像像素（rgb值）如果是png图像，要再加一个h参数
            data.append([x/256.0,y/256.0,z/256.0])
    f.close()
    return np.mat(data),m,n
 
imgData,row,col = loadData(r"C:\Users\10536\Desktop\MSc_Project\py\temp\scan_70_1.jpg")
label = KMeans(n_clusters=5).fit_predict(imgData)  #聚类，获得每个像素的类别（有5类）
label = label.reshape([row,col]) 
plt.imshow(label)
datal = label
np.save(r"C:\Users\10536\Desktop\MSc_Project\py\temp\sacn70_k.npy",datal)
pic_new = image.new("L", (row, col))
# 将图像缩小为0-1之间的数
for i in range(row):
    for j in range(col):
        pic_new.putpixel((i,j), int(256/(label[i][j]+1)))  
pic_new.save(r"C:\Users\10536\Desktop\MSc_Project\py\temp\scan_70_3.jpg", "JPEG") #保存
