# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:51:55 2019

@author: TongDist
"""

def quick_sort(nums):
    # 封装一层的目的是方便用户调用
    def qsort(lst, begin, end):
        if begin >= end:
            return
        i = begin
        key = lst[begin]
        for j in range(begin+1, end+1):
            if lst[j] < key:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[begin], lst[i] = lst[i], lst[begin]
        qsort(lst, begin, i-1)
        qsort(lst,i+1,end)
    qsort(nums, 0, len(nums)-1)
test_list=[9,1,4,6,3,5,7,3]
quick_sort(test_list)
print(test_list)