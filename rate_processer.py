# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 05:20:19 2019

@author: 10536
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
from scipy import signal

def rate_proc(rate):
    b, a = signal.butter(8, 0.15, 'lowpass') 
    filtedData = signal.filtfilt(b, a, rate) 
    print("rate is filted")
    return filtedData
