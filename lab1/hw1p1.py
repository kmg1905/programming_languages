#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 02:41:10 2020

@author: mkondeti
"""

import re
hashSet = set(['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import',
 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try',
 'while', 'with', 'yield'])
identifier = input('enter a identifier: ')

if re.match('^[^\d\W]\w*\Z', identifier) and identifier not in hashSet:
    print(True)
else:
    print(False)

        
    