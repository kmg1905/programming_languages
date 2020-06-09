#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 22:53:07 2020

@author: mkondeti
"""
def check():
    data = input('Enter some string: ')
    data2 = input('Enter some string: ')
    
    if len(data) == 0 or len(data2) == 0:
        if len(data2) == 0:
            if data[0] != '"' or data[0] != data[-1]:
                print(False)
                return
        if len(data) == 0:
            if data2[0] != '"' or data2[-1]!= '"':
                if data2[0] != "'" or data2[-1] != "'":
                    print(False)
                    return
    else:
        if data[0] != "'" or data[-1] != '\\' :
            if data[0] != '"' or  data[-1] != '\\' :
                print('False')
                return
        if data2[-1] != "'" or data[-2] == '\\':
            if data2[-1] != '"' or  data[-2] == '\\':
                print(False)
                return
            
    if len(data) == 0 or len(data2) == 0:
        if len(data) == 0:
            res = data2[:]
        else:
            res = data[:]
    else:
        res = data[:-1] + data2[:]
    if res[0] != res[-1]:
        print(False)
        return
    res = res[1:-1]
    
    nums = []
    for char in res:
        nums.append(char)
    
    for i in range(1, len(nums)):
        if nums[i-1] == '\\' and nums[i] == "'":
            nums[i-1] = '$'
            nums[i] = '$'
        elif nums[i-1] == '\\' and nums[i] == '"':
            nums[i-1] = '$'
            nums[i] = '$'
        elif nums[i-1] == '\\' and nums[i] == "\\":
            nums[i-1] = '$'
            nums[i] = '$'
        elif nums[i-1] == "'" and nums[i] == "'":
            nums[i-1] = '$'
            nums[i] = '$'
        elif nums[i-1] == '"' and nums[i] == '"':
            nums[i-1] = '$'
            nums[i] = '$'
            
    flag = True
    for i in range(len(nums)):
        if nums[i] == "'" or nums[i] == '"':
            flag = False
            break
    if flag:        
        print(True)
    else:
        print(False)
        
check()