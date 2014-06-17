from random import random
from math import log, e


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

# va Poisson ~ (l)

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



#Proceso Poisson 2do metodo con los primeros tiempos de arribos hasta t = T

def procPoisson2(l, T):
    lT = vaPoisson(l)
    n = vaPoisson(T*l)
    uniform_list = []
    for i in range(n):
        uniform_list.append(random())
    res = map(lambda x: x*T, uniform_list)
    res.sort()
    return res

#print procPoisson2(3, 5)
