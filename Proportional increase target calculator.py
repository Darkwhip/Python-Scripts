tgt=int(input("Enter target value: "))
time=int(input("Enter time to hit target: "))
prop=float(input("Enter percentage increase: "))

val=tgt/pow((prop/100)+1, time)

print("The number is %.2f" % val)
