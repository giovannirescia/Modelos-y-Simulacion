from random import random
from math import e, log10

#Generar una va Poisson a partir de un proceso
#de Poisson de media l


def vaPoisson(l):
    i = 0
    u = random()
    acc = u
    while  acc >= pow(e, -l):
        i += 1
        acc *= random()
    return i

for i in range(20):
    print vaPoisson(3)
