# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 02:42:30 2019

@author: 10536
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

def m_filter(img):
    pass
#    img = np.float32(img)
    dst = cv2.medianBlur(img,7)
    return dst

def highpass_filter(img):
    x = cv2.Sobel(img,cv2.CV_16S,1,0)
    y = cv2.Sobel(img,cv2.CV_16S,0,1)
    absx = cv2.convertScaleAbs(x)
    absy = cv2.convertScaleAbs(y)
    dist=cv2.addWeighted(absx,0.5,absy,0.5,0)
    return dist

def get_rate2(img):
    img = img*255/5
#    img = np.transpose(img)
#    rate_m = np.transpose(img)
    rate_m = m_filter(img.astype(np.float32))
    rate_h = highpass_filter(rate_m)
    m = img.shape[0]
    n = img.shape[1]
    rate_r = np.zeros(n)  
    for i in range(n):
        for j in range(m):
            if rate_h[j,i] != 0:
                rate_r[i] = j
                continue
    print("get rate 2")
    return rate_r
    




