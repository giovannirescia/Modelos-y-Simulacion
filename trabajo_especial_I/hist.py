import matplotlib.pylab as mtl
import numpy as np
import simulation as s1
import simulation2 as s2
import simulation3 as s3

l1 = []
l2 = []
l3 = []
for i in range(10**4):
    l1.append(s1.simulation())
    l2.append(s2.simulation())
    l3.append(s3.simulation())

#mtl.axis([0,10,0,0.6])
mtl.title('Comparacion entre los tres sistemas')
mtl.xlabel('Tiempo en meses')
mtl.ylabel('Frecuencia observada')
#mtl.grid(True)

mu1, sigma1 = 1.751, 1.604
mu2, sigma2 = 2.582, 2.459
mu3, sigma3 = 3.597, 3.326

#mtl.text(7, .4, '$\mu=1.751$', size = 25)
#mtl.text(7, .34, '$\sigma=1.604$', size=25)

mtl.hist(l1,100,normed=1 ,facecolor='blue',alpha=0.4, )
mtl.hist(l2,100,normed=1,facecolor='orange',alpha=0.4,  )
mtl.hist(l3,100,normed=1,facecolor='green',alpha=0.4)

mtl.axvline(np.mean(l1), color='blue', linestyle='dashed', linewidth=2, label='Media con dos maquinas de repuesto y un operario (sistema actual)')
mtl.axvline(np.mean(l2),color='orange',linestyle='dashed',linewidth=2, label='Media con dos maquinas de repuesto y dos operarios (primer solucion propuesta)')
mtl.axvline(np.mean(l3),color='green',linestyle='dashed',linewidth=2, label='Media con tres maquinas de repuesto y un operario (segunda solucion propuesta)')

mtl.legend(loc=0, prop={'size': 14})

mtl.show()

