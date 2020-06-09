#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hw1pb2

@author: mkondeti
"""

def checkBinary(number):
    if number[2:] == '':
        print(None)
        return
    
    for i in range(2, len(number)):
        if number[i] == '0' or number[i] == '1':
            pass
        else:
            print(None)
            return
    print('int')
    return

def checkOctal(number):
    if number[2:] == '':
        print(None)
        return
    for i in range(2, len(number)):
        if number[i] < '0' or number[i] > '7':
            print(None)
            return 
    print('int')
    return 
    
def checkHexa(number):
    if number[2:] == '':
        print(None)
        return
    for i in range(2, len(number)):
        if number[i].isalpha():
            if number[i].lower() < 'a' or number[i].lower() > 'f':
                print(None)
                return 
        elif number[i].isnumeric() or number[i] != '.':
            if number[i] < '0' or number[i] > '9':
                print(None)
                return
        else:
            print(None)
            return
    print('int')
    return


def legalInt(number):
    
    if number[0] == '0':
        if number[1].lower() == 'b':
            checkBinary(number)
        elif number[1].lower() == 'o':
            checkOctal(number)
        elif number[1].lower() == 'x':
            checkHexa(number)
        else:
            print(None)
    else:
        
        hashSet = set(['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', 
            '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', 
            ';', '?', '#', '$', ')', '/'])
        for i in range(len(number)):
            if number[i].isalpha() or number[i] in hashSet:
                print(None)
                return
        print('int')
        return
   


def checkDot(number, startIndex):
    for i in range(startIndex, len(number)):
        if number[i].isalpha():
            print(None)
            return
        elif (not number[i].isnumeric()) and number[i] != '.':
            print(None)
            return        
    print('float')
    return


def checkE(number, startIndex):
    for i in range(startIndex, len(number)):
        if number[i].isalpha() and (number[i] != 'e' and number[i] != '-'):
            print(None)
            return
        elif (not number[i].isnumeric()) and (number[i] != 'e' and number[i] != '-'):
            
            print(None)
            return  
        elif number[i] == '-' and number[i - 1] == 'e':
            pass
            
    print('float')
    return
    
    

def legalFloat(number, startIndex):
    
    if '.' in number:
        checkDot(number, startIndex)
    elif 'e' in number:
        checkE(number, startIndex)
    else:
        
        print(None)
    return
    
    
number = input('enter a number: ')
if len(number) == 0:
    print(None)
charIndex = 0   
flag = True

if not number[0].isnumeric():
    for i in range(len(number)):
        if not number[i].isnumeric():
            if number[i] == '+' or number[i] == '-':
                charIndex += 1
            else:
               
                print(None)
                flag = False
                break
        else:
            break
if flag:
    number = number[charIndex:]
     
    startIndex = 0
    for i in range(len(number)):
        if number[i] == '0':
            startIndex += 1
        else:
            break
            
    if startIndex == len(number):
        print('int')
           
    elif '.' in number or 'e' in number or startIndex > 1:
        legalFloat(number, startIndex)
    elif '.' not in number or 'e' not in number:
        
        legalInt(number)
    else:
        print(None)