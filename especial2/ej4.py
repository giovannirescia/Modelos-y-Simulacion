from __future__ import division
from random import random, choice
import matplotlib.pyplot as mpl
import numpy as np
from scipy import stats
from ej3 import *
ganancias = open('ganancia-ins-500.dat')

ganancias = (map(float,(ganancias.read().splitlines())))

#n, bins, patches = mpl.hist(ganancias,75,normed=1 ,facecolor='blue',alpha=0.4, )
#mpl.axvline(np.mean(ganancias), color='blue', linestyle='dashed', linewidth=2, label='Muestra con 100 variables aleatorias geometricas con parametro 0.4')

#mpl.show()
mu, sigma = normal(ganancias)
print mu, sigma
#stats.norm.cdf(loc=

def cumulative(x):
    return stats.norm.cdf(x)
#normalizamos
sigma = np.std(ganancias)
for i in range(len(ganancias)):
    ganancias[i] = (ganancias[i] - mu)/sigma
ganancias.sort()

#print sample

def est_d(l,):
    D = []
    for i in range(500):
        D.append((i+1)/500 - l[i])
        D.append(l[i] - (i)/500)
    return max(D)


def ej8():
    l = [random() for i in range(500)]
    l.sort()
    return est_d(l)
Y = map(cumulative, ganancias)
d = est_d(Y)

r = 1000
hits = 0
print d
for i in range(r):


    D = ej8()

    if D >= d:
        hits += 1
print hits/r
