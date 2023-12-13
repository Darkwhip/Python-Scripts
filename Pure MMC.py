# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 10:53:21 2022

@author: Filippe
"""

def numCapture(amount):
    c=[]
    b=""
    for i in range(len(amount)):
        a=amount[i]
        if a!="," and b!="":
            b=b+a
        elif a!=",":
            b=a
        else:
            c.append(int(b))
            b=""
    c.append(int(b))
    return c

def primeGen(cap):
    prime = [2,3,5]
    for i in range(6,cap):
        for k in range(len(prime)):
            if i % prime[k] == 0:
                break
            elif k+1 == len(prime):
                prime.append(i)
    return prime

def allOne(array):
    for i in range(len(array)):
        if array[i] !=1:
            return False
    return True

def isDivisible(array, div):
    for i in range(len(array)):
        if array[i] % div == 0:
            return True
    return False

numbers = []
size = int(input("Enter how many numbers you desire to input: "))
input0 = input("Type the numbers separated by a comma: ")
numbers=numCapture(input0)
primes = primeGen(max(numbers))
mmc=1
while allOne(numbers)==False:
    for k in range(len(primes)):
        while isDivisible(numbers, primes[k]):
            for i in range(len(numbers)):
                if numbers[i] % primes[k] == 0:
                    numbers[i] = numbers[i]/primes[k]
            mmc=mmc*primes[k]
print("Least common multiplier: ", mmc)