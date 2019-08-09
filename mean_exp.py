# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 03:56:52 2019

@author: 10536
"""
import numpy as np
import read_bin
import figure_processer
import rate_processer
import Kmeans_pro
import rate_processer_2
import matplotlib.pyplot as plt
import get_file
import Data_save


def mean_pro(file_name,path):
    fin = read_bin.read_bin2(file_name,path)
    scan70 = fin[:,70,:].astype(np.float32)
    img_h = figure_processer.hist_eq(scan70*255)
    img_gamma = figure_processer.gamma(img_h,0.8)
    img_bright = figure_processer.bright(img_gamma,2.5,0/255)
    img_m = figure_processer.m_filter(img_bright.astype(np.float32))
    img_hp = figure_processer.highpass_filter(img_m*255)/255
    rate = figure_processer.get_rate1(img_hp)
    np.savetxt(r"%s_rate_1.txt"%(path),rate.astype(np.int),fmt='%d')
    rate_f = rate_processer.rate_proc(rate)
    np.savetxt(r"%s_rate_f.txt"%(path),rate_f.astype(np.int),fmt='%d')
    rate_2 = Kmeans_pro.Kmeans_pro(img_h,5)
    plt.figure()
    plt.title('%s'%(file_name))
    plt.imshow(rate_2)
    plt.show()
    rate2 = rate_processer_2.get_rate2(rate_2)
    np.savetxt(r"%s_rate_2.txt"%(path),rate2.astype(np.int),fmt='%d')
    print("%s done"%(file_name))
    return rate,rate_f,rate2,img_h
    
for file in get_file.getFiles(r"C:\Users\10536\Desktop\MSc_Project\files", '.bin'):
    path = file[0]
    print(path)
    file_name = file[1]
    print(file_name)
    Data_save.save_data_selected(file_name,path)
#    rate,rate_f,rate2 = mean_pro(file_name,path)
#    break
##path = r"C:\Users\10536\Desktop\MSc_Project\files\example_dia_motion_A"
##file_name = r"example_dia_motion_A"
##rate,rate_f,rate2,img_h = mean_pro(file_name,path)

