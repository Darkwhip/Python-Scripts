import math as m
import time as t

r1=float(input("Enter first vector magnitude: "))
t1=int(input("Enter first vector angle: "))
r2=float(input("Enter second vector magnitude: "))
t2=int(input("Enter second vector angle: "))
print("1 - Cartesian")
ch=int(input("Enter desired solving method: "))
ref=t.monotonic()
if ch == 1:
    x1=r1*m.cos(m.radians(t1))
    y1=r1*m.sin(m.radians(t1))
    x2=r2*m.cos(m.radians(t2))
    y2=r2*m.sin(m.radians(t2))
    x3=x1+x2 #Componente X da soma
    y3=y1+y2 #componente Y da soma
else:
    exit
print("Vector sum = ", x3,", ", y3)
r3=m.sqrt(m.pow(x3,2)+m.pow(y3, 2)) #Hipotenusa do trinagulo pro modulo do vetor
t3=m.degrees(m.atan(y3/x3))
print("Vector sum in polar = ", r3,", ", t3,"°")
ref=t.monotonic()-ref
print("Calculation took ",ref,"s")
