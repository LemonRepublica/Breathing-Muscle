# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 17:40:40 2019

@author: 10536
"""
def get_fpb(file_name,path):
    filein = open(r"%s.txt"%(path),'r')
    #fileout = []              # 返回一个文件对象   
    lines = filein.readlines()               # 调用文件的 readline()方法   
    infor = []
    #for line in lines:
    #    if line == '\n':
    #        line = line.strip("\n")
    #    print(line)
    if lines :
        last_line = lines[-12:]
    for line in last_line:
        if line.split():
            print(line)
            infor.append(line)
    num_frame = int(infor[0].lstrip("[FRAME_NUMBER_").rstrip("]\n"))+1
    num_points = int(infor[3].lstrip("INPUT_POINTS_PER_BEAM="))
    num_beams = int(infor[4].lstrip("INPUT_BEAMS_PER_FRAME="))
    #    line = filein.readline()   
   
    filein.close()
    fpb = [num_frame,num_points,num_beams]
    print("get info from %s.txt"%(file_name))
    return fpb

