from __future__ import division
from random import random
from math import log, e
from scipy import stats
import numpy as np
import matplotlib.pyplot as mpl
import matplotlib.mlab as mlab


# frecuencias de observaciones en una muestra
def freq(obs):
    N = []
    obs_vals = list(set(obs))
    for i in obs_vals:
        N.append(obs.count(i))
    return N

# lista de densidades
def densidades(valores_posibles, p):
    densidades = []
    for x in valores_posibles:
        densidades.append(stats.geom.pmf(x, p))
    return densidades

def gen_geom(size, p):
    geoms = list(stats.geom.rvs(p, size=size))
    return geoms


def estadistico_t(freq_list, p_list, n):

    t = 0.0
    for i in range(len(p_list)):
        a = (freq_list[i] - n*(p_list[i]))**2
        b = n*p_list[i]
        t += a/b
    return t

def get_T(n):
    geoms = gen_geom(n, 0.4)
    geoms_freqs = freq(geoms)
    geoms_absolute_vals = list(set(geoms))
    geoms_dens = densidades(geoms_absolute_vals, 0.4)
    t = estadistico_t(geoms_freqs, geoms_dens, n)
    return t


#geoms = gen_geom(10**2, 0.4)
#geoms = map(lambda x: (x - 2.5) / 3.74, geoms)
#print geoms
#print stats.chisquare(geoms_freqs)
n=10**4
t=get_T(n)
print "Observacion t de los datos para tener una t_obs con cual comparar T", t

hits = 0
R = 10**3

for i in range(R):
    T=get_T(n)
    if T>=t:
        hits += 1

print hits/R
