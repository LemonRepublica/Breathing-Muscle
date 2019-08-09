# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 03:30:32 2019

@author: 10536
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
import skimage.measure as measure

def gamma(img,x):
#use gamma correction to enhance the figure
    scan_gamma = np.power(img/np.max(img), x)
    return scan_gamma

def bright(img,alpha,beta):
    blank = np.zeros(img.shape,img.dtype)#创建图片类型的零矩阵

    dst = cv2.addWeighted(img,alpha,blank,1-alpha,beta)
    for i in range(dst.shape[0]):
        for j in range(dst.shape[1]):
            if dst[i,j] > 1:
                dst[i,j] = 1
            else:
                dst[i,j] = dst[i,j]/2
    return dst

def m_filter(img):
#    pass
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

def hist_eq(img):
#    for i in range(img.shape[0]):
#        for j in range(img.shape[1]):
#            img[i,j] = np.uint8(img[i,j]*255)
    img_h = cv2.equalizeHist(img.astype(np.uint8))
    return img_h

def get_rate1(img):
    rate = np.zeros(img.shape[1])
    for i in range(img.shape[1]):
        label = img[:,i]
        if i == 0:
            label_sel = max(label)
        else:
            up = int(max(0,rate[i-1]-100))
            down = int(min(rate[i-1]+100,len(rate)))
            label_sel = max(label[up:down])
        for j in range(img.shape[0]):            
            if img[j,i] == label_sel:
                rate[i] = j
#                if (i < 262)&(i > 252):
#                    print(j)
#                    print(rate[i])
#                continue
    print("get rate")
#    plt.plot(rate)
    return rate


def crop(img):
    m = img.shape[0]
    n = img.shape[1]
    cropped = img[int(m*0.4):m,0:n]
    return cropped

def sigma(data):
#    plt.plot(data,'b')
    data2 = data
    k = 30
    data_ref = data2[0:k]
    for i in range(1,len(data2)-1):
        datamean = np.mean(data_ref)
        datastd = np.std(data_ref)
        threshold1 = datamean - 3 * datastd
        threshold2 = datamean + 3 * datastd
        if (data2[i] < threshold1)|(data2[i] > threshold2):
            if (((data2[i] - data2[i-1])<0)&((data2[i+1] - data2[i])>0))|(((data2[i] - data2[i-1])>0)&((data2[i+1] - data2[i])<0)):
                data2[i] = int((data2[i-1] + data2[i+1])/2)

        if i < k:
            data_ref = data2[0:k]
        else:
            data_ref = data2[i-k:i]
    return data2

#cv2.imshow('sacn70',img_gamma)
#cv2.imshow('sacn70',img_hp)
#plt.imshow(scan70)
    

def largestConnectComponent(bw_img):


    labeled_img, num = measure.label(bw_img, neighbors=4, background=0, return_num=True)    
    # plt.figure(), plt.imshow(labeled_img, cmap = 'gray')

    max_label = 0
    max_num = 0
    for i in range(1, num): # start from 1 to avoid set the background as component
        if np.sum(labeled_img == i) > max_num:
            max_num = np.sum(labeled_img == i)
            max_label = i
    lcc = (labeled_img == max_label)

    return lcc.astype(np.int16)

def Binarization(img):
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if i > 0.4 * img.shape[0]:
                if img[i,j] > 0.49:
                    img[i,j] = 1
            else:
                img[i,j] = 0

    return img

def resize_fin(fin):
    frames = fin.shape[2]
    fin_sq = np.zeros((512,512,frames))
    for i in range(frames):
        fin_sq[:,:,i] = cv2.resize(fin[:,:,i],(512,512))
    return fin_sq

def get_scan_line(img_masked):
    frames = img_masked.shape[2]
    line1 = np.zeros(frames)
    for i in range(frames):
        moment = cv2.moments(img_masked[:,:,i])
        line1[i] = int(moment['m10'] / moment['m00'])
    line_mean = np.mean(line1)
    line_std = np.std(line1)
    line_sum = np.sum(line1)
    threshold1 = line_mean - 3 * line_std
    threshold2 = line_mean + 3 * line_std
    items = frames
    for i in range(frames):
        if (line1[i] < threshold1)|(line1[i] > threshold2):
            line_sum = line_sum - line1[i]
            items = items - 1
    scan_line = line_sum / items
    return scan_line.astype(np.int16)
            
    
    