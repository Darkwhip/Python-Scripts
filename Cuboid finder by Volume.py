size=int(input("Enter desired volume: "))
for i in range(0, size):
    for j in range(0, size):
        for k in range(0, size):
            if i*j*k==size:
                print(i, "x", j,"x",k, "=", size)
            elif i*j*k>size:
                break
            
