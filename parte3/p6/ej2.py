from random import random
from math import e


def integral():
    u = random()
    return e**pow(u,2)


def ej2():
    x = integral()
    m = x
    s = 0
    for i in range(2,101):
        x = integral()
        a = m
        m = m + (x - m)/float(i)
        s = (1 - 1/(float(i)-1))*s + i*(m -a)**2
    i = 30.0
    while pow(s/i,0.5) > 0.01:
        i += 1
        x = integral()
        a = m
        m = m + (x - m)/i
        s = (1 - 1.0/(i - 1))*s + i*((m - a)**2)
    return (i, m, s)


N = 10**3
suma = 0.0
for i in range(N):
    a,b,c= ej2()
    suma = suma + a
print "Esperanza", suma/N
print "numero de datos: ", a
print "media: ", b
print "varianza: ", c
