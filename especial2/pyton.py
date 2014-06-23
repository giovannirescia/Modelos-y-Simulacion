from scipy.stats import geom
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)


p = 0.5
mean, var, skew, kurt = geom.stats(p, moments='mvsk')


x = np.arange(geom.ppf(0.01, p),
              geom.ppf(0.99, p))
print x
print geom.pmf(x,p)
ax.plot(x, geom.pmf(x, p), 'bo', ms=8, label='geom pmf')
ax.vlines(x, 0, geom.pmf(x, p), colors='b', lw=5, alpha=0.5)


rv = geom(p)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1,
        label='frozen pmf')
ax.legend(loc='best', frameon=False)

