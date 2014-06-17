from __future__ import division
from random import random
from math import e
from scipy import stats

def est_d(l, n):

    D = []
    for i in range(n):
        D.append((i+1)/n - l[i])
        D.append(l[i] - (i)/n)
    return max(D)

def exp(x):
    return 1 - pow(e, -x/50.0)


def ej4(n):

    l = [random() for i in range(n)]
    l.sort()
    return est_d(l, n)

sample = [86,133,75,22,11,144,78,122,8,146,33,41,99]
sample.sort()
n = len(sample)
d_list = []
Y = map(exp, sample)

for i in range(n):
    y_i = Y[i]
    d_list.append((i+1)/n - y_i)
    d_list.append(y_i - (i)/n)
d = max(d_list)


r = 5000
hits = 0
print d
for i in range(r):
    if ej4(n) >= d:
        hits += 1
print hits/r
    
