from random import random
from math import log


#PROCESO DE POISSON NO HOMOGENEO
def procPoisson(l, T, f):
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
            if v < f(t)/l:
                I += 1
                S[I] = t
    return S

#Funcion de densidad ejercicio 12 practico 5
def funcion_intensidad(t):
    return 3 + 4/(t+1)



def varianza():
    s = 0.0
    N = 10**3
    for i in range(N):
        s+=len(procPoisson(30, 10, funcion_intensidad))
    media = s/N

    s2 = 0.0
    for i in range(N):
        s2 += (len(procPoisson(30,10,funcion_intensidad)) - media)**2
    return s2/N

print varianza()
