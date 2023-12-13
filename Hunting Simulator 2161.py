import random as pony
from array import array

birb= [0 for y in range(5)]
sloth = ["Radroaches","Radhogs","Radscorpions","Manticore","Deathclaw"]
bat=int(input("Number of Hunters: "))
sand=int(input("Number of weeks to simulate: "))
murkrow=0 #sum of meats
for y in range(sand):
	for i in range(bat):
		fate=pony.randint(1, 6)
		if fate<4:
			birb[fate-1]=birb[fate-1]+pony.randint(1,4)
		elif fate>4:
			birb[fate-2]=birb[fate-2]+pony.randint(1,4)
print("We caught: ")
for i in range(len(birb)):
	print(str(birb[i]) + " - " + sloth[i])
	murkrow=murkrow+birb[i]
print("Total: ", murkrow)