from __future__ import division
from scipy import stats
from matplotlib.pylab import plt
import numpy as np
from math import log
from random import random

g1 = stats.geom.rvs(0.4, size=10**2)

g2 = stats.geom.rvs(0.4, size=10**3)

g3 = stats.geom.rvs(0.4, size=10**4)


#calcular el limite teorico de la geometrica

def geo():
    u = random()
    a = log(u)
    b = log(1-0.4)
    return int(a / b) + 1


gt = []
for i in range(10**4):
    gt.append(geo())
#print gt
x = [g1,g2,g3,gt]
common_params =dict(bins=35, normed=1,histtype='bar', alpha=0.7,range=(0,18), color=['blue','green','red','orange'],align='right',label=['Muestra de 100 Geoms.','Muestra de 1000 Geoms.','Muestra de 10000 Geoms.','Muestra teorica'])

plt.subplots_adjust(hspace=.4)
#plt.title('Skinny shift - 3 at a time')
#plt.hist((g1, g2, g3, gt), **common_params)
#plt.subplot(313)
# 100 Geometricas
#plt.hist(g2, 35,normed=1, facecolor='green',alpha=0.7,width=0.2)
plt.hist(g1, 35,normed=1 , facecolor='b',alpha=0.7,width=0.2)
#plt.hist(gt,35,normed=1,facecolor='grey',alpha=0.6,width=0.2 )
#plt.hist(g3, 35,normed=1, facecolor='b',alpha=0.7,width=0.2)



plt.title('Histograma con 100 variables Aleatorias Geometricas de parametro 0.4')

#plt.axvline(np.mean(g3), color='orange', linestyle='dashed', linewidth=2)
#plt.hist(x, **common_params)
#plt.legend()
plt.show()
