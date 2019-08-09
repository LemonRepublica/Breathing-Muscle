# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 02:46:37 2019

@author: 10536
"""

import subprocess
import get_file
import Data_save


for file in get_file.getFiles(r"C:\Users\10536\Desktop\MSc_Project\MSc", '.tvd'):
    print(file)
    print("\n")
    path = file[0]
    file_name = file[1]
    cmd = [r"b_to_cre.exe", r"/ip=%s.tvd"%(path), r"/op=C:\Users\10536\Desktop\MSc_Project\files\%s.bin"%(file_name)]
    p = subprocess.run(cmd, shell=True)
    Data_save.save_data(file_name)

