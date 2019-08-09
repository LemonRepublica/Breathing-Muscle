# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 02:12:45 2019

@author: 10536
"""

import numpy as np
import read_bin
import PIL.Image as image
import figure_processer
import get_mask
import Kmeans_pro
import get_file

#file_name = "usnd_190604_150518"

def save_data(file_name,path):
    fin = read_bin.read_bin2(file_name,path)
    row = fin.shape[0]
    col = fin.shape[1]
    frames = fin.shape[2]
    for i in range(frames):
        label = fin[:,:,i] 
        img_h = figure_processer.hist_eq(label*256)
        pic_new = image.new("L", (row, col))
        for j in range(row):
            for k in range(col):
                pic_new.putpixel((j,k), int((img_h[j][k]+1))) 
        new_img = pic_new.resize((512,512),image.BILINEAR)
        new_img = new_img.transpose(image.ROTATE_270)
        new_img = new_img.transpose(image.FLIP_LEFT_RIGHT)
        new_img.save(r"C:\Users\10536\Desktop\MSc_Project\py\data_set\%s__%d.jpg"%(file_name,i), "JPEG")
        print("save %d"%(i))
        
def save_data_selected(file_name,path):
    fin = read_bin.read_bin2(file_name,path)
    row = fin.shape[0]
    col = fin.shape[1]
    frames = fin.shape[2]
    z = 0
    sel = np.linspace(120,frames-140,5)
    sel = sel.astype(np.int)
    for i in sel:
        z = z+1
        label = fin[:,:,i] 
        img_h = figure_processer.hist_eq(label*256)
        pic_new = image.new("L", (row, col))
        for j in range(row):
            for k in range(col):
                pic_new.putpixel((j,k), int((img_h[j][k]+1))) 
        new_img = pic_new.resize((512,512),image.BILINEAR)
        new_img = new_img.transpose(image.ROTATE_270)
        new_img = new_img.transpose(image.FLIP_LEFT_RIGHT)
        new_img.save(r"C:\Users\10536\Desktop\MSc_Project\py\data_selected\%s__%d.jpg"%(file_name,z), "JPEG")
        print("save %d"%(i))
        
def save_data_masked(file_name,path):
    fin = read_bin.read_bin2(file_name,path)
    row = fin.shape[0]
    col = fin.shape[1]
    frames = fin.shape[2]
    z = 0
    sel = np.linspace(120,frames-140,5)
    sel = sel.astype(np.int)
    for i in sel:
        z = z+1
        label = fin[:,:,i] 
        img_h = figure_processer.hist_eq(label*256)
        img_mask = Kmeans_pro.Kmeans_pro(img_h,3)
        img_m = figure_processer.m_filter(img_mask.astype(np.float32))
        pic_new = image.new("L", (row, col))
        for j in range(row):
            for k in range(col):
                pic_new.putpixel((j,k), int((img_m[j][k]*255/3+1))) 
        new_img = pic_new.resize((512,512),image.BILINEAR)
        new_img = new_img.transpose(image.ROTATE_270)
        new_img = new_img.transpose(image.FLIP_LEFT_RIGHT)
        new_img.save(r"C:\Users\10536\Desktop\MSc_Project\py\data_Kmeans\%s__%d_mask.jpg"%(file_name,z), "JPEG")
        print("save %d"%(i))
    
for file in get_file.getFiles(r"C:\Users\10536\Desktop\MSc_Project\files", '.bin'):
    path = file[0]
    print(path)
    file_name = file[1]
    print(file_name)
    save_data_selected(file_name,path)

    
    
