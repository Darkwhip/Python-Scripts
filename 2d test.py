import math as m

tiles=[]
for i in range(-6,7):
    for j in range(-6,7):
        if round(m.sqrt((i-0)**2+(j-0)**2), 0)<=7:
            tiles.append([i,j])
print(tiles, "," ,len(tiles))
