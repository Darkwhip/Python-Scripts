def primeToNumber(limit):
    a=[2, 3, 5]
    for i in range(6, limit):
        prime=True
        for j in range(0, len(a)):
            if i % a[j] == 0:
                prime=False
                break
        if prime:
            a.append(i)
    return a

lista=primeToNumber(14)
print(lista)
