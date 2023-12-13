import time

def soma():
    tot= 0
    for i in range(1, 1000000001):
        tot += i
    return tot

ts=time.time()
res = soma()
te=time.time()
print("Soma = ", res)
print("Tempo = ", te-ts)
