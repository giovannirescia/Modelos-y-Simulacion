from __future__ import division
from random import random, choice
import matplotlib.pyplot as mpl
import numpy as np
from scipy import stats
from ej3 import *
import matplotlib.pylab as mlab


ganancias = open('ganancia-ins-500.dat')

ganancias = (map(float,(ganancias.read().splitlines())))

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
#print d
for i in range(r):


    D = ej8()

    if D >= d:
        hits += 1
print hits/r
