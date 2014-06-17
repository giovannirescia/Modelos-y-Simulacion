from __future__ import division
from random import random

# calculo de t
def estadistico_t(freq_list, p_list, n):

    t = 0.0
    for i in range(len(p_list)):
        a = (freq_list[i] - n*(p_list[i]))**2
        b = n*p_list[i]
        t += a/b
    return t


def ej1(p_j, n):

    values = [int(random()*4) + 1 for i in range(n)]
    N = []

    for i in range(1,5):
        N.append(values.count(i))
    N[1] = N[1] + N[2]
    N.pop(2)

    T = 0.0

    return estadistico_t(N, p_j, n)

original_N = [141, 291, 132]
p_j = [1/4, 1/2, 1/4]

s = 0.0

n = 564
t = estadistico_t(original_N, p_j, n)

r = 10000
hits = 0

for k in range(r):
    T = ej1(p_j, n)
    if T >= t:
        hits += 1
print hits/r
