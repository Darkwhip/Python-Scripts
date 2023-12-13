# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:08:11 2021

@author: Filippe
"""
line = []
triangle = []
i, j = 0, 0
size = int(input("How tall is the triangle? "))
for i in range(size): #Cycling Lines
    for j in range(i+1): #Cycling Columns
        #print("Calculating value for ", i, " ", j)
        if j == 0 or j == i:
            line.append(1)
        else:
            line.append(triangle[i-1][j-1]+triangle[i-1][j])
    triangle.append(line)
    line=[]
for i in range(size):
    print(triangle[i]," = ", sum(triangle[i]))