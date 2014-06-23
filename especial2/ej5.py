from __future__ import division
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pylab as mlab
import numpy as np

ganancias = open('ganancia_media.dat')

ganancias = (map(float,(ganancias.read().splitlines())))
max_g = max(ganancias)
min_g = min(ganancias)

bins = (max_g - min_g) / 0.1
fig = plt.figure()
a, bins, patches = plt.hist(ganancias,15,range=(365, 366.5), normed=1,facecolor='green',alpha=0.4, label='Medias semanales')
plt.title('Normalidad asintotica de la media muestral')

#Graficamos la funcion de densidad de la normal
mu = np.mean(ganancias)
sigma = np.std(ganancias)

print mu
print sigma**2
bins = [365 + i / 100.0 for i in range(151)]
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r', color='red', label='Normal')

ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)


ax.set_xlabel('Medias Semanales')

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


plt.legend()
plt.show()
