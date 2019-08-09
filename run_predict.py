# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 22:27:36 2019

@author: 10536
"""
import read_bin
import numpy as np
import cv2
from keras.models import load_model
import figure_processer
import matplotlib.pyplot as plt


class do_predict(object):
    def __init__(self,fin):
        self.fin_sq = fin_sq
        self.frames = fin_sq.shape[2]
        self.col = fin_sq.shape[1]
        self.row = fin_sq.shape[0]
        

    def run_predict(self):
        #load the trained model from .hdf5 file
        model = load_model(r"C:\Users\10536\Desktop\MSc_Project\py\Unet\my_test\my_unet.hdf5")
        model.summary()
        pack = np.zeros((self.frames,self.col,self.row,1))
        #model.predict requires the input in a format of [frames,size,size,1]
        for i in range(self.frames):
            #resize each frame to 512*512
            img_h = figure_processer.hist_eq(self.fin_sq[:,:,i]*255)
            #enhance the picture
            pack[i,:,:,0] = img_h/(255)
        pre_y = model.predict(pack, batch_size=1, verbose=1)
        return pre_y
    
    def do_mask(self,pre_y):
        img_masked =  np.zeros((self.col,self.row,self.frames))
        for i in range(self.frames):
            img_org = pre_y[i,:,:,0]
            #transform the predicted value to 0-1 and corp the top value
            img_bin = figure_processer.Binarization(img_org)
            #select the largest area as diaphgram
            img_mask = figure_processer.largestConnectComponent(img_bin)
            #use the bit calculation to cut the orginal image
            img_masked[:,:,i] = cv2.bitwise_and(img_mask*255,(self.fin_sq[:,:,i]*255).astype(np.int16))
        return img_masked
    
            

            


#read in the binary file to predict
path = r"C:\Users\10536\Desktop\MSc_Project\files\example_dia_motion_C"
file_name = "example_dia_motion_C"
fin = read_bin.read_bin2(file_name,path)
fin_sq = figure_processer.resize_fin(fin)
item1 = do_predict(fin_sq)
pre_y = item1.run_predict()
img_masked = item1.do_mask(pre_y)
scan_line = figure_processer.get_scan_line(img_masked)
rate_1_1 = figure_processer.get_rate1(img_masked[:,scan_line,:])
rate_1_1_m = figure_processer.sigma(rate_1_1)
#bbb = pre_y[0,:,:,0]
#img_bin = figure_processer.Binarization(bbb)
#img_mask = figure_processer.largestConnectComponent(img_bin)
plt.imshow(img_masked[:,:,0])
    