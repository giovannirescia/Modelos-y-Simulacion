from random import random
from math import log

#PROCESO DE POISSON NO HOMOGENEO
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
            v = random()
            if v < (3+4/(t+1))/float(l):
                I += 1
                S[I] = t
    return S


s = 0.0
N = 10**3
for i in range(N):
    s+=len(procPoisson(30, 10))

print s/N
