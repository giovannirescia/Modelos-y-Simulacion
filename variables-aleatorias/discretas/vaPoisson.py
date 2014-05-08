from random import random, seed
from math import e

def vaPoisson(l):
    u = random()
    i = 0
    p = pow(e, -l)
    F = p
    while u >= F:
        p = p*l/(i + 1)
        F = F + p
        i = i + 1    
    return i


def factorial(i):
    if i == 0:
        return 1
    else:
        return i*factorial(i-1)


def recursiveP_i(i, l):
    if i==0:
        p = pow(e, -l)
    else:
        p = (recursiveP_i(i-1, l)*l)/i
    return p


#Optimized algotithm


def vaPoisson2(l):
    i = int(l)
    F = 0.0
    p = recursiveP_i(i,l)
    for j in range(0, i+1):
        F += recursiveP_i(j, l)
    u = random()
    res = 0
    print "U -------->",repr(u)
    print "lambda -------->",repr(l)
    if u <= F:
        print "CASE U <= F \r\n"
        while u <= F:
            F = F - p
            p = (p*i)/l
            i = i - 1
        res = i

    elif u > F:
        print "CASE U > F\r\n"
        while u > F:
            p = (p*l)/(i + 1)
            F = F + p
            i = i + 1 
        res = i

    return i

for i in range(3):
    
    print vaPoisson2(int(random()*10)+8)
