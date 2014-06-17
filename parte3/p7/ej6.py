from __future__ import division
from random import random
from math import e, log

def exp():
    x = random()
    return -log(x)

def exp2(x):
    return 1 - pow(e, -x)

def est_d(l, n):
    D = []
    for i in range(n):
        D.append((i+1)/n - l[i])
        D.append(l[i] - (i)/n)
    return max(D)

def ej6(n):

    l = [random() for i in range(n)]
    l.sort()
    return est_d(l, n)

n = 10
sample = [exp() for i in range(n)]

sample.sort()
Y = map(exp2, sample)

d = est_d(Y, n)

r = 1000
hits = 0
print d
for i in range(r):
    D = ej6(n)
    if D >= d:
        hits += 1
print hits/r
