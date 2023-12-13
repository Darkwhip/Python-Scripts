def get_TimeSec(time):
    c=""
    sec=0
    for i in range(0, len(time)):
        if time[i] == 'h':
            c=int(c)*3600
            sec=sec+c
            c=""
        elif time[i] == 'm':
            c=int(c)*60
            sec=sec+c
            c=""
        elif time[i] == 's':
            sec=sec+int(c)
            c=""
        else:
            c=c+time[i]
        ##print(c)
    return sec

def primeToNumber(limit):
    a=[2, 3, 5]
    for i in range(6, limit):
        prime=True
        for j in range(0, len(a)):
            if i % a[j] == 0:
                prime=False
                break
        if prime:
            a.append(i)
    return a

wa = input("Time of first factory: ")
wb = input("Time of second factory: ")

wa.replace(" ","")
wb.replace(" ","")
wat=get_TimeSec(wa)
wbt=get_TimeSec(wb)
wa, wb = wat, wbt
if wat>wbt:
    a=primeToNumber(wat)
else:
    a=primeToNumber(wbt)
s=1
while wat and wbt > 1:
    c=0
    for i in range(0, len(a)):
        if wat % a[i] == 0 and wbt % a[i] == 0:
            c=a[i]
            break
    if c == 0:
        for i in range(0, len(a)):
            if wat % a[i] == 0:
                c=a[i]
                break
            elif wbt % a[i] == 0:
                c=a[i]
                break
    print(wat," ",wbt," ",c," ",s)
    if wat % c == 0:
        wat=wat/c
    if wbt % c == 0:
        wbt=wbt/c
    s=s*c
print("Least Common Multiple: ", s)
print("The ratio is = ",s/wa,"/",s/wb)
print("Ratio alternative A = 1 /", (s/wa)/(s/wb))
print("Ratio alternative B = 1 /", (s/wb)/(s/wa))
