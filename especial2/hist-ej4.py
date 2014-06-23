from __future__ import division
from random import random, choice
import matplotlib.pyplot as mpl
import numpy as np
from scipy import stats
from ej3 import normal, gamma, lognormal
import matplotlib.pylab as mlab
import math

ganancias = open('ganancia-ins-500.dat')

ganancias = (map(float,(ganancias.read().splitlines())))

#grafica de las ganancias
n, bins, patches = mpl.hist(ganancias,bins=34, range=(345, 379), normed=1 ,facecolor='yellow',alpha=0.7, label='Muestra de las Ganancias')

#Graficamos la funcion de densidad de la normal
mu = np.mean(ganancias)
sigma = np.std(ganancias)
y = mlab.normpdf(bins, mu, sigma)
mpl.plot(bins, y, 'r', color='red', label='Normal')


#grafica de la funcion lognormal
lognorm_mu, sigma_logn = lognormal(ganancias)
y2 = stats.lognorm.pdf(bins,sigma_logn**0.5, 0, np.exp(lognorm_mu))
mpl.plot(bins, y2, 'r', color='green', label='Lognormal')

#grafica de la funcion gamma
alpha, lambd = gamma(ganancias)
y3 = stats.gamma.pdf(bins, alpha,0, 1 / lambd)
mpl.plot(bins, y3, 'r', color='blue', label='Gamma')

mpl.legend(loc=0, prop={'size': 14})

mpl.title('Comparacion de los modelos de ajuste')

mpl.show()
