import matplotlib.pyplot as mpl
import numpy as np

ganancias = open('ganancia-ins-500.dat')

ganancias = (map(float,(ganancias.read().splitlines())))
ganancias = np.array(ganancias)
mpl.title('Independencia de los datos')
mpl.scatter(ganancias[1:], ganancias[:-1], alpha=0.4,color='g', marker='<')
mpl.show()

