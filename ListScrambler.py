# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 06:56:56 2023

@author: Filippe
"""
import random as r

def scramble(li):
    for i in range(len(li)):
        j=r.randint(0, len(li)-1)
        l=li[j]
        li[j]=li[i]
        li[i]=l
    return li