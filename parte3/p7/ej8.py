from __future__ import division
from random import random
from scipy import stats
import numpy as np


def est_d(l, n):
    D = []
    for i in range(n):
        D.append((i+1)/n - l[i])
        D.append(l[i] - (i)/n)
    return max(D)


def cumulative(x):
    return stats.norm.cdf(x)


sample = [91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7]
observations = len(sample)

u_est = sum(sample)/observations
sample_array = np.array(sample)
sigma_est = np.std(sample_array)
print observations

#normalizamos
for i in range(observations):
    sample[i] = (sample[i] - u_est)/sigma_est
sample.sort()

#print sample
Y = map(cumulative, sample)

d = est_d(Y, observations)

def ej8(n):
    l = [random() for i in range(n)]
    l.sort()
    return est_d(l, n)


r = 1000
hits = 0
print d
for i in range(r):
    D = ej8(observations)
    if D >= d:
        hits += 1
print hits/r
