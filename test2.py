# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 15:35:28 2019

@author: TongDist
"""
from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle 
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time
import sys
import os
import time
import random
       
def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        for filename in files:
            fh = CreateFile(filename, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0) 
            createTime, accessTime, modifyTime = GetFileTime(fh) 
            createTime = Time(time.mktime(time.gmtime(random.uniform(1514780000,1546300000))))
            accessTime = Time(time.mktime(time.gmtime(random.uniform(1514780000,1546300000))))
            modifyTime = Time(time.mktime(time.gmtime(random.uniform(1514780000,1546300000))))
            SetFileTime(fh, createTime, accessTime, modifyTime) 
            CloseHandle(fh)
            #print(type(files[1]))
        #print(root) #当前目录路径  
        #print(dirs) #当前路径下所有子目录  
         #当前路径下所有非目录子文件  
file_name("C:/Users/TongDist/Desktop/past/图片")
