import math as m

Acc = float(input("Enter accuracy in degrees: "))
h = float(input("Enter range: "))

y = 2*m.sqrt(m.pow(h/m.sin(m.radians(90-Acc/2)), 2)-m.pow(h, 2))

print("It projects a ", y, "m circle at a range of ", h, "m with an accuracy of ", Acc,"°")
