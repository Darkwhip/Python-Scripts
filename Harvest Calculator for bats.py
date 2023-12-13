import random as pony
from array import array

ferret=input("Is it normal? (Y/Null) ")
dog=int(input("How many plants per type? "))
cat=int(input("How many types? "))
snek=int(input("How many plants does one harvest yield? "))
fish=int(input("How many days? "))
bat = [[0 for x in range(2)] for y in range(cat)] #sums table common, plus
fish=int(fish/2)
hippo=0 #Plus plant harvest
maus=0 #Normal plant harvest
#print(bat)
pony.seed()
for birb in range(0, fish):
    for evil in range(0, cat):
        for good in range(0, dog):
            fox=False
            if pony.randint(1, 4)<4: #effect number 3 check
                hippo=hippo+1
                fox=True
            elif pony.randint(1, 2)<2 and (ferret=='y' or ferret=='Y'): #Check N3 on non-plus
                hippo=hippo+1
                fox=True
            if pony.randint(1, 4)<4: #effect number 4 boosted by 5
                if fox:
                    hippo=hippo+pony.randint(1, 3)
                else:
                    maus=maus+pony.randint(1, 3)
            maus=maus+snek
        #print(evil)
        bat[evil][0]=bat[evil][0]+maus
        bat[evil][1]=bat[evil][1]+hippo
        maus,hippo = 0,0

fledermaus = 0
for evil in range(0, cat): #Output loop
    print("Plant #",evil," = ",bat[evil][0]*2.1," common, ",bat[evil][1]*2.1," plus")
    maus=bat[evil][0]*2.1+maus  #10% from mettle-life-touch and double from happiness
    fledermaus=bat[evil][1]*2.1+fledermaus
print("Greengel gained: ",((dog*cat*fish)/5)-5*fish)
print("Generic food sum: ",maus)
print("Plus food sum: ",fledermaus)
print("Now counting mettle 10% bonus!")
