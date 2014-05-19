from random import random, seed
from math import log

def procPoisson(l, T):
    t = 0
    I = 0
    S = {}
    done = True
    while done:
        u = random()
        if t - (1.0/l)*log(u) > T:
            done = False
        else:
            t -= (1.0/l)*log(u)
            I += 1
            S[I] = t
    return S


def ej11():
    x = 0.0
    s = 0.0
    c = len(procPoisson(5,1))
    for i in range(c):
        x += int(21*random())+20
    return x



def varianza():
    s = 0.0
    N = 10**3
    for i in range(N):
        s+=ej11()
    media = s/N

    s2 = 0.0
    for i in range(N):
        s2 += (ej11() - media)**2
    return s2/N


print varianza()
