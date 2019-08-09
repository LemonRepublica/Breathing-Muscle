# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 01:57:41 2019

@author: 10536
"""

import numpy as np

def get_mask(img):
    m = img.shape[0]
    n = img.shape[1]
    thres = max(map(max,img))*0.5
    img_mask = img
    for i in range(n):
        for j in range(m):
            if img[j,i] < thres or j<250:
                img_mask[j,i] = 0
#            else img_mask[j,i] = 255
    return img_mask
                