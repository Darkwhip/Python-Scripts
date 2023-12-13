def Triangle(Num):
    if Num<=1:
        return 1
    else:
        return Triangle(Num-1)+Num


N1=int(input("Insert n for triangle number n(x): "))
for i in range(N1-5, N1+5):
    print("Triangle number ", i ," is ", Triangle(i),";")
