from __future__ import division
from random import random
from math import log, exp
from scipy import stats

ganancias = open('ganancia-ins-500.dat')

ganancias = (map(float,(ganancias.read().splitlines())))
"""

OBTENER EL ESTADISTICO d Y EL p-valor PARA LA MUESTRA
AJUSTANDO A LAS DISTRIBUCIONES: NORMAL, LOGNORMAL Y
GAMMA.

"""
def normal(data):
    x = sum(data)/len(data)
    sigma2 = 0
    for xi in data:
        sigma2 += (xi - x)**2 / len(data)
    return (x,sigma2)

mu, sigma2 = normal(ganancias)
sigma = sigma2**0.5
print "KS NORMAL"
print stats.kstest(ganancias, 'norm',args=(mu,sigma))



def lognormal(data):
    data = map(log, data)
    x = sum(data) / len(data)    
    sigma2 = 0
    for xi in data:
        sigma2 += (xi - x)**2 / len(data)
    return (x,sigma2)

mu, sigma2 = lognormal(ganancias)
print mu, sigma2
sigma = sigma2**0.5

data = map(log, ganancias)
print "KS LOGNORMAL"
print stats.kstest(data, 'norm',args=( mu,sigma))


def gamma(data):
    # media
    x = sum(data) / len(data)
    x_logaritmizadas = map(log, data)

    la_media_de_las_x_logaritmizadas = sum(x_logaritmizadas) / len(data)

    A = log(x) - la_media_de_las_x_logaritmizadas

    aux = 1 / (4*A)
    aux2 = (1 + 4*A / 3)**0.5
    alpha = aux * ( 1 + aux2)
    l = alpha / x
    return (alpha , l)

alp, lam = gamma(ganancias)
print alp, lam
print "KS GAMMA"
print stats.kstest(ganancias, 'gamma', args=(alp,0,1 /lam))
