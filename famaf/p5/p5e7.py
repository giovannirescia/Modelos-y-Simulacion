from random import random
from math import log, e

#Metodo de aceptacion y rechazo
#f(x) = xe**-x
#g(x) = 1/2 * e**-x/2 (exponencial (1/2))
#h(x) = f(x)/g(x) = 2*x*e**-x/2
#h'(x) = (2 -x)e**-x/2
#pto critico x = 2
#valor maximo c = e/4
#h(x)/c = 2xe**-x/2 * e / 4

def ej7():
    u1 = random()
    u2 = random()
    y = -2*log(u1)
    while u2 >= e*y*pow(e, -y/2)/2:
        u1 = random()
        u2 = random()
        y = -2*log(u1)
    return y


for i in range(29):
    print ej7()
