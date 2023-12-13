# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:29:36 2022

@author: Filippe
"""

import math as m

theta=int(input("Input angle: "))
r=int(input("Input distance: "))
x=r*m.cos(m.radians(theta))
y=r*m.sin(m.radians(theta))
print("(" ,x, ", " ,y, ")")