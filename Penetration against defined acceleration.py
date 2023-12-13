import math
m = math

print("Welcome to penetration depth against determined acceleration calculator")
print("Still need to lower those titles...")
accel=float(input("Insert Acceleration in m/s² : "))
dist=float(input("Insert the distance which the object travels, in m : "))
invel=float(input("Insert object starting speed in m/s: "))
brk = invel/accel
print("Time to stop object : ", brk,"s")
pen = (invel * brk) - (((1/2)*accel)*(brk**2))
print("Penetration distance : ", pen, "m")
