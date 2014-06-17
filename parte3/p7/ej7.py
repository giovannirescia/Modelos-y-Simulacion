from __future__ import division
from random import random
from math import log, e


def exp(l):
    x = random()
    return (-1.0/l)*log(x)

def exp2(x):
    return 1 - pow(e, -x*0.093225)

def est_d(l, n):
    D = []
    for i in range(n):
        D.append((i+1)/n - l[i])
        D.append(l[i] - (i)/n)
    return max(D)

def est_l(l):
    return pow(sum(l)/len(l), -1)


def ej7(n):
    l = [random() for i in range(n)]
    l.sort()
    return est_d(l, n)

sample = [1.6,10.3,3.5,13.5,18.4,7.7,24.3,10.7,8.4,4.9,7.9,12,16.2,6.8,14.7]

est_lambda = est_l(sample)
print est_lambda
n = 15
sample.sort()
Y = map(exp2, sample)

d = est_d(Y, n)

r = 1000
hits = 0
print d
for i in range(r):
    D = ej7(n)
    if D >= d:
        hits += 1
print hits/r
