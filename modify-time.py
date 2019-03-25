# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 15:35:28 2019

@author: TongDist
"""
from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle 
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time
import os
import time
import random
from os import path 

start_time=1514780000
latest_time=1546300000
 
start=random.uniform(start_time,latest_time)
modify_time=start+random.uniform(0,latest_time-start)
access_time=modify_time+random.uniform(0,latest_time-modify_time)
for root, dirs, files in os.walk(path.dirname(__file__)):  
    for filename in files:
        if filename!="test.py":
            fh = CreateFile(filename, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0) 
            createTime, accessTime, modifyTime = GetFileTime(fh)
            
            createTime = Time(time.mktime(time.gmtime(start)))
            modifyTime = Time(time.mktime(time.gmtime(modify_time)))
            accessTime = Time(time.mktime(time.gmtime(access_time)))
            
            SetFileTime(fh, createTime, accessTime, modifyTime) 
            CloseHandle(fh)
