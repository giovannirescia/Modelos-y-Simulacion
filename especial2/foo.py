import numpy as np
import matplotlib.pyplot as plt
mydata = np.array([6.36,6.34,6.36,6.73,7.36,6.73])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(mydata, weights=np.zeros_like(mydata) + 1. / mydata.size)
n, bins, patches = ax.hist(mydata, bins=100, normed=1, cumulative=0)

ax.set_xlabel('Bins', size=20)
ax.set_ylabel('Frequency', size=20)
ax.legend

plt.show()
