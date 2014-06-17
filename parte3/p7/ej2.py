from __future__ import division
from random import random

def estadistico_t(freq_list, p_list, n):

    t = 0.0
    for i in range(len(p_list)):
        a = (freq_list[i] - n*(p_list[i]))**2
        b = n*p_list[i]
        t += a/b

    return t


def ej2(p_list, n):

    l = [int(random()*6)+1 for i in range(n)]
    N = []
    for i in range(1,7):
        N.append(l.count(i))

    return estadistico_t(N, p_list, n)

p_list = [1/6 for i in range(6)]

NN = [158, 172, 164, 181, 160, 165]
n = 1000
t = estadistico_t(NN, p_list, n)

r = 1000
hits = 0.0
for i in range(r):
    if ej2(p_list, n) > t:
        hits += 1
print "p-valor", hits/1000
