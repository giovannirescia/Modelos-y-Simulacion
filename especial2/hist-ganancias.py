from __future__ import division
from random import random
from math import log, exp
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pylab as P

ganancias = open('ganancia-ins-500.dat')

ganancias = np.array((map(float,(ganancias.read().splitlines()))))


num_bins = 50
#n, bins, patches = plt.hist(ganancias, num_bins, normed=1, facecolor='green', alpha=0.5)


mu = np.mean(ganancias)
sigma = np.std(ganancias)
# the histogram of the data

#y = mlab.normpdf(bins, mu, sigma)
#P.plot(bins, y, 'r-', )

# lognormal

mu2 = 5.9029
sigma2 = 0.01109
dist = stats.lognorm([sigma2],loc=mu2)
y2 = np.linspace(345, 380, 500)

#alpha_ = alpha(data)
#lambda_ = lamba(data)
#y = stats.gamma.pdf(bins, alpha_, scale=1.0 / lambda_)
#P.plot(bins, y, 'r-', color='chartreuse', label='Gamma')
P.plot(y2, dist.pdf(y2))
P.show()
