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

path = r"C:\Users\10536\Desktop\MSc_Project\files\example_dia_motion_B"
file_name = "example_dia_motion_B"

fin = read_bin.read_bin2(file_name,path)
scan70 = fin[:,45,:].astype(np.float32)
img_crop = figure_processer.crop(scan70)
img_h = figure_processer.hist_eq(img_crop*255)
####img_gamma = figure_processer.gamma(img_h,1.2)
####img_bright = figure_processer.bright(img_gamma,1.5,0/255)
####img_m = figure_processer.m_filter(img_bright.astype(np.float32))
####img_hp = figure_processer.highpass_filter(img_m*255)/255
####rate = figure_processer.get_rate1(img_hp)
####rate_m = figure_processer.sigma(rate)
####np.savetxt(r"%s_rate_1.txt"%(path),rate_m.astype(np.int),fmt='%d')
#rate_1 = figure_processer.get_rate1(img_gamma)

rate_1_1 = figure_processer.get_rate1(img_h)
rate_1_1_m = figure_processer.sigma(rate_1_1)
#return the cropped value back
rate_1_1_m = rate_1_1_m + 0.4 * scan70.shape[0]
np.savetxt(r"%s_rate_2.txt"%(path),rate_1_1_m.astype(np.int),fmt='%d')
rate_1_2 = figure_processer.get_rate1(img_crop)
#plt.plot(rate_1_2,'r')
rate_1_2_m = figure_processer.sigma(rate_1_2)
rate_1_2_m = rate_1_2_m + 0.4 * scan70.shape[0]
#plt.plot(rate_1_2,'g')
np.savetxt(r"%s_rate_3.txt"%(path),rate_1_2_m.astype(np.int),fmt='%d')
#np.savetxt(r"%s_rate_1.txt"%(path),rate.astype(np.int),fmt='%d')
#rate_f = rate_processer.rate_proc(rate)
#np.savetxt(r"%s_rate_f.txt"%(path),rate_f.astype(np.int),fmt='%d')
#img_m_2 = rate_processer_2.m_filter(img_h.astype(np.float32))
#rate_2 = Kmeans_pro.Kmeans_pro(img_crop,3)
#plt.figure()
#plt.title('%s'%(file_name))
#plt.imshow(rate_2)
#plt.show()
###rate2_m = figure_processer.m_filter(rate_2.astype(np.float32))
###rate2_hp = figure_processer.highpass_filter(rate2_m)
###rate2_m = figure_processer.m_filter(rate_2.astype(np.float32))
###rate2_hp_2 = figure_processer.highpass_filter(rate_2.astype(np.float32))
###rate2 = rate_processer_2.get_rate2(rate2_hp)
###rate2_2 = rate_processer_2.get_rate2(rate2_hp_2)
#np.savetxt(r"%s_rate_2.txt"%(path),rate2.astype(np.int),fmt='%d')
print("%s done"%(file_name))
#plt.plot(rate_1_2,'g')
