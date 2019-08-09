# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 18:00:12 2019

@author: 10536
"""
import numpy as np
import matplotlib.pyplot as plt
import read_txt

def read_bin(file_name,path):
    fpb = read_txt.get_fpb(file_name,path)
    num_frame = fpb[0]
    num_points = fpb[1]
    num_beams = fpb[2]
    f = open(r"%s.bin"%(path),"rb")
    ffin = np.zeros((num_points,num_beams,num_frame))
    fin = f.read(num_points*num_beams*num_frame)
    #frame1 = np.zeros(884*96)
    for l in range(num_frame):
        for k in range(num_beams):
            for j in range(num_points):
                ffin[j,k,l] = fin[num_beams*num_points*l+num_points*k+j]/255
    f.close()
    print("read_1 file %s.bin"%(file_name))
    return ffin

def read_bin2(file_name,path):
    fpb = read_txt.get_fpb(file_name,path)
    num_frame = fpb[0]
    num_points = fpb[1]
    num_beams = fpb[2]
    f = open(r"%s.bin"%(path),"rb")
    ffin = np.zeros((num_points,num_beams,num_frame))
    #frame1 = np.zeros(884*96)
    for l in range(num_frame):
        for k in range(num_beams):
            fin = f.read(num_points)
            finn = np.array(list(map(float,fin)))
            ffin[:,k,l] = finn/255
    f.close()
    print("read_2 file %s.bin"%(file_name))
    return ffin
