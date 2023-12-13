import math as m
import random as r

r.seed()
p=[]
lim=100

p.append([r.randint(-lim,lim),r.randint(-lim,lim)])
p.append([r.randint(-lim,lim),r.randint(-lim,lim)])

midpoint=[(p[0][0]+p[1][0])/2,(p[0][1]+p[1][1])/2]
print(p[0], ", ", p[1], ", ", midpoint, ".")
dist=m.sqrt((pow((p[1][0]-p[0][0]), 2)+pow((p[1][1]-p[0][1]), 2)))
distm=m.sqrt((pow((p[1][0]-midpoint[0]), 2)+pow((p[1][1]-midpoint[1]), 2)))
print("distance between points: ",dist,".\ndistance between second point and middle:",distm,".")
