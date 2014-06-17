from __future__ import division
from random import random


def est_d(l, n):

    D = []
    for i in range(n):
        D.append((i+1)/n - l[i])
        D.append(l[i] - (i)/n)

    return max(D)

def ej3(n):
    l = [random() for i in range(n)]
    l.sort()
    return est_d(l, n)

muestra = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
muestra.sort()
n = len(muestra)

d = est_d(muestra, n)

hits = 0
r = 500
print d
for i in range(r):
    D = ej3(n)
    if D >= d:
        hits += 1
print hits/r
