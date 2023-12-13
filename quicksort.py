# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 06:49:59 2023

@author: Filippe
"""
import GenerateList as g
import ListScrambler as s
import random as r
import time

def quicksort(li):
    if len(li)==1:
        return li
    liA=[]
    liB=[]
    pivot=r.randrange(len(li))
    for i in range(len(li)):
        if i!=pivot:
            if li[i]<=li[pivot]:
                liA.append(li[i])
            else:
                liB.append(li[i])
    if len(liA)>1:
        #print("liA: ", liA,", Pivot: ", li[pivot])
        liA=quicksort(liA)
    if len(liB)>1:
        #print("liB: ", liB,", Pivot: ", li[pivot])
        liB=quicksort(liB)
    liA.append(li[pivot])
    return liA+liB

#li=s.scramble(g.gen(1000000))
li=g.gen(1000000)
#print("Original: ", li)
ts=time.time()
li=quicksort(li)
te=time.time()
#print(li)
print("Time = ", te-ts,"s")
