import numpy as np

X=int(input("Define X: "))
Y=int(input("Define Y: "))
Z=int(input("Define Z: "))
t=np.zeros((X, Y, Z))
f = open("(" + str(X) + ", " + str(Y) + ", " + str(Z) +") Table", 'w')
f.write(str(t))
f.close()