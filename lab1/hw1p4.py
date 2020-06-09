#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 02:21:06 2020

@author: mkondeti
"""
    

def parsedate(date):
    
    tempdate = date.split('/')
    if len(tempdate[0]) <= 1:
        print(None)
        return
    if len(tempdate[1]) <= 1:
        print(None)
        return
    if len(tempdate[2]) <= 3:
        print(None)
        return
    from datetime import datetime
    try:
        dt = datetime.strptime(date, '%m/%d/%Y')
    except ValueError:
        print(None)
        return
    val = dt.weekday()
    weekday = ''
    if val == 0: 
        weekday = 'Monday'
    elif val == 1: 
        weekday = 'Tuesday'
    elif val == 2: 
        weekday = 'Wednesday'
    elif val == 3: 
        weekday = 'Thursday'
    elif val == 4: 
        weekday = 'Friday'
    elif val == 5: 
        weekday = 'Saturday'
    elif val == 6: 
        weekday = 'Sunday'
    else:
        print('date error')
        return
        
    month = ''
    
    if dt.month == 1:
        month = 'January'
    elif dt.month == 2:
        month = 'February'
    elif dt.month == 3:
        month = 'March'
    elif dt.month == 4:
        month = 'April'
    elif dt.month == 5:
        month = 'May'
    elif dt.month == 6:
        month = 'June'
    elif dt.month == 7:
        month = 'July'
    elif dt.month == 8:
        month = 'August'
    elif dt.month == 9:
        month = 'September'
    elif dt.month == 10:
        month = 'October'
    elif dt.month == 11:
        month = 'November'
    elif dt.month == 12:
        month = 'December'
    else:
        print('month error')
        return
        
    print(weekday + ", " + month + " " + str(dt.day) + ", "+ str(dt.year))
    
date = input('Enter complete date MM/DD/YYYY: ')
parsedate(date)