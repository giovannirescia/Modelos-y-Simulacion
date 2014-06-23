from __future__ import division
from random import random, choice
import numpy as np

# estadistico r
def rango(x, nm_list):
    r = 0
    for k in x:
        index = nm_list.index(k)
        r += index + 1
    return r


def p_n_m(n, m, r):
    if n >= 1 and m == 0:
        if r > 0:
            return 1
        else:
            return 0
    elif n == 0 and m >= 1:
        if r < 0:
            return 0
        else:
            return 1
    else:
        return (n / float(n + m)) * p_n_m(n - 1, m, r - m - n) +\
            (m / float(n + m)) * p_n_m(n, m - 1, r)


def valor_p(n, m, r):
    return 2 * min([p_n_m(n, m, r), 1 - p_n_m(n, m, r - 1)])


x = [65.2, 67.1, 69.4, 78.4, 74, 80.3]
y = [59.4, 72.1, 68, 66.2, 58.5]
#x = sorted([132, 104, 162, 171, 129])
#y = sorted([107, 94, 136, 99, 114, 122, 108, 130, 106, 88])

n = len(x)
m = len(y)
xy = sorted(x + y)

r = rango(x, xy)

print valor_p(n, m, r)

def normal_r(r, n, m):
    a = r - n*(n+m+1)/2
    b = pow(n*m*(n + m + 1)/12, 0.5)
    return a/b

def rnd_std_nor():
    return np.random.normal(loc=0, scale=1.0)


def valor_p_distribucion_R(n, m, r):
    N = n + m
    rr = (r - (n * (N + 1)) / 2.0) / (math.sqrt((n * m * (N + 1)) / 12.0))
    if r <= n * (N + 1) / 2.0:
        return 2 * stats.norm.cdf(rr)
    else:
        return 2 * (1 - stats.norm.cdf(rr))

print "ola"
print valor_p_distribucion_R(x, y, r)
#print r
k = 1000
hits = 0
r_n = normal_r(r, 5, 10)
#print r_n
#for i in range(k):
#    ns = rnd_std_nor()
#    if ns >= r_n:
#        hits += 1


#print valor_p(n, m, r)



def by_simulation(x, y):
    n = len(x)
    m = len(y)
    x_rand = [int((n+m)*random()) + 1 for j in range(n)]
    return sum(x_rand)


for w in range(k):
    R = by_simulation(x, y)
    if R > r:
        hits += 1
print hits/k

