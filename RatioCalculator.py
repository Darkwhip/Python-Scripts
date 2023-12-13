def primeGen(n):
    p = [2,3,5,7]
    for i in range(7,n):
        for j in range(len(p)):
            if i%p[j]==0:
                break
        else:
            p.append(i)
    return p

def allOne(n):
    for i in range(len(n)):
        if n[i]!=1:
            return False
    return True

def mmcCalc(n, p):
    ans=1
    while allOne(n)==False:
        for i in range(len(p)):
            div=False
            for j in range(len(n)):
                if n[j]%p[i]==0 and n[j]!=1:
                    n[j]=n[j]/p[i]
                    div=True
            if div:
                ans=ans*p[i]
    return ans

print("Welcome to Ratio finder, this program gives the ratio of the first number to the second number")
print("For example, a ratio of 2:1 = 0,5")
s= int(input("Number of values to balance: "))
fn=[]
for i in range(s):
    print("Insert number", i,": ")
    fn.append(int(input()))
fn.sort(reverse=True)
primes=primeGen(fn[0]+1)
primes.reverse()
mmc=mmcCalc(fn.copy(),primes)
print("MMC = ", mmc)
print("Original = ", fn)
for i in range(len(fn)):
    fn[i]=(mmc/fn[i])
print("Ratio: ", fn)
