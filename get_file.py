# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 19:29:44 2019

@author: 10536
"""

import os

def getFiles(dir, suffix):
#fins root and suffix
    res = []
    for root, directory, files in os.walk(dir):  
    #search all the files in the path
        for filename in files:
            name, suf = os.path.splitext(filename) 
            #return filename, path
            if suf == suffix:
                res.append((os.path.join(root, name),name)) 
                #return the joined path and filename(w/o suffix)
    return res
