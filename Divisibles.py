n=int(input("Insert number: "))
for i in range(n):
    if i>1 and n%i==0:
        print(i, " = ", n/i)
