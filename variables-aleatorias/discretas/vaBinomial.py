from random import random


def recursiveP_i(i, n, p):

    if i == 0:
        res = (1 -p)**n
    else:
        res = ((n - i)*p/(i + 1)*(1 - p))*(recursiveP_i(i-1, n, p))
    return res


def binomial(n, p):
    u = random()
    i = 0
    c = p/(1 - p)
    pr = (1 - p)**n
    f = pr
    while u >= f:
        pr = (c*(n-1)/(i+1))*pr
        f += f + pr
        i += 1
    return i

#Optimization

def binomial2(n, p):
    
for i in range(25):
    print binomial(25, 0.32)
