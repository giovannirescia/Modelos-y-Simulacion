from random import random
from math import e
from recursive_mean_var import mean, var
def integral():
    u = random()
    return e**pow(u,2)

def ej2():
    N = 10**2
    l = [integral() for j in range(N)]
    media = mean(l)
    s = var(l)
    i = float(len(l))
    new_mean = media
    while s/pow(i,0.5) >= 0.01:
        x = integral()
        i += 1
        new_mean = media + (x - media)/i
        s = (1 - 1.0/(i-1))*s + i*(new_mean - media)**2
    return (i, new_mean, s)


N = 10**3
suma = 0.0
for i in range(N):
    a,b,c= ej2()
    suma = suma + a
print "Esperanza", suma/N
print "numero de datos: ", a
print "media: ", b
print "varianza: ", c
