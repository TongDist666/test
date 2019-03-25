# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 18:18:09 2019

@author: TongDist
"""

import numpy as np

from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle 
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
from pywintypes import Time
import os
import time
import random

#先check,再change
#检查count数
def check_count(check_count_file_dir):
    
    #如果count存在，读并返回count的内容
    if os.path.exists(check_count_file_dir):
        check_count_file_read=open(check_count_file_dir,'r')
        check_count_str=check_count_file_read.readline()
        if check_count_str:
            #print('now count is:  '+check_count_str)
            return int(check_count_str)
        else:
            return 0
        
    #如果check不存在，创建count，但返回0
    else:
        with open(check_count_file_dir,'w') as check_count_file_write:
            check_count_file_write.write('0')
            print('Not exist:'+check_count_file_dir+'!\nAnd now create it.')
        return 0
#更新count数
def change_count(change_count_file_dir,pre_count_int):
    with open(change_count_file_dir,'w') as change_count_file_write:
        now_count=pre_count_int+1
        change_count_file_write.write(str(now_count))
        print('Change the count from '+str(pre_count_int)+' to '+str(now_count))
        return now_count
#修改文件时间
def get_create_acess_modify_time():
    start_time=1514780000
    latest_time=1546300000
    
    start=random.uniform(start_time,latest_time)
    modify_time=start+random.uniform(0,latest_time-start)
    access_time=modify_time+random.uniform(0,latest_time-modify_time)
    return [start,modify_time,access_time]
def modify_model_file_time(model_file_dir):
    for root, dirs, files in os.walk(model_file_dir):
        start_time=1514780000
        latest_time=1546300000
        for filename in files:
            if filename!='untitled1.py':
                fh = CreateFile(filename, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0) 
                createTime, accessTime, modifyTime = GetFileTime(fh)
                
                start=random.uniform(start_time,latest_time)
                
                createTime = Time(time.mktime(time.gmtime(start)))
                
                modify_time=start+random.uniform(0,latest_time-start)
                modifyTime = Time(time.mktime(time.gmtime(modify_time)))
                
                access_time=modify_time+random.uniform(0,latest_time-modify_time)
                accessTime = Time(time.mktime(time.gmtime(access_time)))
                
                SetFileTime(fh, createTime, accessTime, modifyTime) 
                CloseHandle(fh)
modify_model_file_time(os.path.dirname(__file__))
check_count('count.txt')
print(change_count('count.txt',check_count('count.txt')))
check_count('count.txt')