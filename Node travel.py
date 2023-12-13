import random as r
import numpy as n
class node:
    def __init__(self, ident, cx, cy):
        self.id=ident
        self.x=cx
        self.y=cy
        self.addNearNeighbour(self.id)
    def addNearNeighbour(self, tid):
        self.nearNeighbour=tid
    def __str__(self):
        return 'ID = {self.id}, X = {self.x}, Y = {self.y}, Nearest neighbour = {self.nearNeighbour}'.format(self=self)

def populate(towns, x, y):
    t=[]
    for i in range(towns):
        t.append(node(i, r.randrange(0, x), r.randrange(0, y)))
    return t

r.seed()
areax=900
areay=900
cities=populate(100,areax,areay)
for i in range(10):
    print(str(cities[i]),"\n")
