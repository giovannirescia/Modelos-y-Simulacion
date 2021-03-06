from __future__ import division
from random import random
from math import log10
from scipy import stats
import numpy as np
import matplotlib.pylab as mpl
import matplotlib.mlab as mlab


def estadistico_t(freq_list, p_list, n):

    t = 0.0
    for i in range(len(p_list)):
        a = (freq_list[i] - n*(p_list[i]))**2
        b = n*p_list[i]
        t += a/b
    return t


def freq(sample):
    N = []
    m = min(sample)
    M = max(sample)
    for i in range(m,M+1):
        N.append(sample.count(i))
    return N


def p_j_list(sample, p):
    intervals = [i for i in range(min(sample), max(sample)+1)]
    p_j_list = []
    for x in intervals:
        p_j_list.append(stats.geom.pmf(x,p))
    return p_j_list


p1 = []
for i in range(1):
    g1 = list(stats.geom.rvs(0.4, size=100))
    pj_g1 = p_j_list(g1, 0.4)
    pj_g1 = map(lambda x: x*100, pj_g1)
    freq_g1 = freq(g1)
    aux = stats.chisquare(freq_g1, pj_g1)
    p1.append(aux[1])

p2 = []
for i in range(1):
    g2 = list(stats.geom.rvs(0.4, size=1000))
    pj_g2 = p_j_list(g2, 0.4)
    pj_g2 = map(lambda x: x*1000, pj_g2)
    freq_g2 = freq(g2)
    aux = stats.chisquare(freq_g2, pj_g2)
    p2.append(aux[1])




s = 0.0
for i in range(1):
    g3 = list(stats.geom.rvs(0.4, size=10000))
    pj_g3 = p_j_list(g3, 0.4)
#    pj_g3 = map(lambda x: x*10000, pj_g3)
    freq_g3 = freq(g3)
    s += estadistico_t(freq_g3, pj_g3,10000)

print s/1000



# 100 Geometricas
#n, bins, patches = mpl.hist(g1,10,normed=1 ,facecolor='blue',alpha=0.4, )
#mpl.axvline(np.mean(g1), color='blue', linestyle='dashed', linewidth=2, label='Muestra con 100 variables aleatorias geometricas con parametro 0.4')

# 1000 Geometricas
#n, bins, patches = mpl.hist(g2,10,normed=1 ,facecolor='green',alpha=0.4, )
#mpl.axvline(np.mean(g2), color='green', linestyle='dashed', linewidth=2, label='Muestra con 1000 variables aleatorias geometricas con parametro 0.4')

# 10000 Geometricas
n, bins, patches = mpl.hist(g3,10,normed=1 ,facecolor='orange',alpha=0.5, )
mpl.axvline(np.mean(g3), color='orange', linestyle='orange', linewidth=2, label='Muestra con 10000 variables aleatorias geometricas con parametro 0.4')





mu = 1 / 0.4
sigma = (1 - 0.4) / 0.4**2
y = mlab.normpdf(bins,mu, sigma)

mpl.plot(bins, y, 'r--')

mpl.legend(loc=7, prop={'size': 12})

#mpl.show()
#t = estadistico_t(g2, p_j_
r = 500
hits = 0

def simul_t():
    g_list = list(stats.geom.rvs(0.4, size=10000))
    pj_g = p_j_list(g_list, 0.4)
    freq_g = freq(g_list)
    pj_g3 = map(lambda x: x*10000, pj_g)
#    print freq_g
    return stats.chisquare(freq_g, pj_g3)


for k in range(r):
    T = simul_t()

    T = T[0]
    if T >= 27.33:
        hits += 1
print hits/r
