import random as pony
from array import array

def defaultOne(number = 1):
    if number == '':
        number = 1
    return int(number)

def pieUpdate(level = 3, plus = "y"):
    global pie, pop, hapi
    pie=hapi
    if plus=="y":
        pie=int(pie-pop/10)
    if level==3:
        pie=int(pie-(pop/5)*3-30) #Floofed
    elif level==2:
        pie=int(pie-(pop/5)*2-5) #Stuffed
    elif level==1:
        pie=int(pie-(pop/5)-3) #Well-fed
    return

def happinessUpdate(level = 3, plus = "y"):
    global pie, pop, hapi, catrice
    if plus=="y":
        pie=int(pie+pop/10)
    if level==3:
        pie=int(pie+(pop/5)*3+30) #Floofed
    elif level==2:
        pie=int(pie+(pop/5)*2+5) #Stuffed
    elif level==1:
        pie=int(pie+(pop/5)+3) #Well-fed
    hapi=pie
    if catrice == 4:
        hapi=hapi+100
    elif catrice == 3:
        hapi=hapi-100
    return
    

def packageParse(choice):
    global res, pop, catrice, events
    opop=pop
    if choice == 0:
        res[2]=res[2]-2000
        res[0]=res[0]+500
        res[1]=res[1]+500
        res[3]=res[3]+40
        res[4]=res[4]+20
        res[5]=res[5]+20
    elif choice == 1:
        res[6]=res[6]+2 #cloth
        res[0]=res[0]+20
        res[1]=res[1]+10
        res[7]=res[7]+1 #rad away
        for i in range(1):
            if catrice==4:
                pop=pop+pony.randint(1, 3)*2
            else:
                pop=pop+pony.randint(1, 3)
    elif choice == 2:
        res[6]=res[6]+4
        res[8]=res[8]+1 # 4 diff meal
        res[9]=res[9]+1 # 2 diff. dessert
        res[2]=res[2]-100
        for i in range(3):
            if catrice==4:
                pop=pop+pony.randint(1, 4)*2
            else:
                pop=pop+pony.randint(1, 4)
    elif choice == 3:
        res[0]=res[0]+50
        res[1]=res[1]+50
        res[10]=res[10]+1
        res[11]=res[11]+5
        for i in range(3):
            if catrice==4:
                pop=pop+pony.randint(1,6)*2
            else:
                pop=pop+pony.randint(1,6)
    elif choice == 4:
        res[0]=res[0]+100
        res[1]=res[1]+100
        res[12]=res[12]+7
        res[6]=res[6]+20
        for i in range(9):
            if catrice==4:
                pop=pop+pony.randint(1,6)*2
            else:
                pop=pop+pony.randint(1,6)
    if choice!=0:
        print(pop-opop, " Ponies gained.")
    events[choice]=events[choice]+1
    return


print("Welcome to Buckingham Manager")
print("For all your simulation needs we require some data first:")
pop=int(input("Number of ponies in settlement = "))
hapi=int(input("Happiness quoficient index = "))
mare=int(input("Catrice's club number of masseurs = "))
res = [0 for x in range(13)] #food-0, water-1, cap-2, explosive-3, electrical comp.-4, crystal-5, cloth-6, rad-away-7, four diff. meal-8, two diff. dessert-9, big desert-10, tier 3 gem home-11, bubbly mana potion-12
derpy=True
events = [0 for x in range(5)] #catrice strip-0, cherry pack-1, picnic blast-2, surprise-3, big one-4
catrice = 0
sand=0
donut=int(input("And before we forget, how would you rate our prosperity? 3 - Floofed, 2 - Stuffed, 1 - Well-fed: "))
corn=input("Did we feed them enhanced rations(y/n)? ") #Happiness status levels and plus food flag
smoothie=True
if input("Population Stagnant(y/n)?")=="y":
	smoothie=False #stagnant pop flag
while derpy:
    guest=0
    for i in range(int(pop/10)):
        guest=guest+pony.randint(1, 4)
    print("Catrice's massage house got ", guest, " visitors.")
    res[0]=res[0]+guest*5
    res[1]=res[1]+guest*5
    res[2]=res[2]+(guest*100)*2 #Happiness effect
    lust=mare*5
    for i in range(guest):
        if lust<1:
            break
        y=pony.randint(1, 20)
        if y==19 or y==18:
            res[2]=res[2]+150*2
            lust=lust-1
        elif y==20:
            res[2]=res[2]+500*2
            lust=lust-1
    pieUpdate(donut, corn) # Pie is happiness minus status and pop
    if smoothie:
	    if catrice==4:
	        pop=pop+(((hapi/10)*(1+(pony.randint(1, 100)/100)))*2) 
	    else:
	        pop=pop+((hapi/10)*(1+(pony.randint(1, 100)/100))) #Pop update based on current happiness
	    happinessUpdate(donut, corn) #update happiness based on new pop
	    package=0
	    mama=True #Can do Big One
	    while package!=5:
	        print("Choose a package for this week:")
	        print("1 - Cherry Pack;")
	        print("2 - picnic blast;")
	        print("3 - S.S.S.S.(Super Secret Sugary Surprise);")
	        if mama:
	            print("4 - The Big One;")
	        print("5 - Continue.")
	        package=int(input("Chose: "))
	        if package > 0 and package <4:
	            for i in range(defaultOne(input("How Many? "))):
	                packageParse(package)
	        elif package==4 and mama:
	            packageParse(package)
	            mama=False
	        elif package!=5:
	            print("Invalid Choice")
    if catrice == 0:
        print("Should Catrice throw a party this week? (y/n)")
        b=input()
        if b=="y":
            catrice=4
            packageParse(0)
    else:
        catrice=catrice-1

    if sand%3==0 and sand>0: #happiness monthly update
        pieUpdate(donut, corn)
        print("\nHappiness quoficient update request:")
        print("Rate Buckingham current prosperity levels:")
        print("1 - Well-fed;")
        print("2 - Stuffed;")
        print("3 - Floofed.")
        donut=int(input("Choice: "))
        corn=input("Are we feeding them GM crops(y/n)? ")
        happinessUpdate(donut, corn)

    print("Simulate another week? N = exit")
    if input("Option: ")=="N":
        derpy=False
    print("End of week", sand, "\n")
    sand=sand+1
print("\n\n\n")
print(sand, "Weeks have passed and the settlement now houses ", pop, " Ponies, Happiness Quoficient Index now rates ", hapi,";")
dinky=["Well-fed", "Stuffed", "Floofed"]; cherry={"y":"Plus food", "n":"Regular food"}
print("Our latest prosperity survey indicates ponies are", dinky[donut-1], "and we've fed them",cherry[corn],";")
print("Catrice hosted an event ", events[0], " times;")
print("Cherry & Co have made: ",events[1], " Cherry Pack(s), ", events[2]," Picnic Blast, ", events[3]," Super Secret Sugary Surprise, ", events[4]," The Big Ones;")
print("During this time the settlement consumed:")
sloth=["Food", "Water", "Caps net", "Explosives", "Electrical components", "Crystals", "Cloth", "Rad-away or Healing potions", "Four different meals", "Two different desserts", "Big deserts", "Tier 3 gems set to go home", "Bubbly mana potions"]
for i in range(len(res)):
    print(res[i], " - ", sloth[i], ";")
print("\nThanks for using Buckingham Manager by BatOS.")
