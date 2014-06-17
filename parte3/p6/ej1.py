import numpy as np
from vanormal import nor_est3


def ej1():

    x = nor_est3()
    s = 0.0
    m = x
    for i in range(2,31):
        x = nor_est3()
        a = m
        m = m + (x - m)/float(i)
        s = (1 - 1/(float(i)-1))*s + i*(m -a)**2
    i = 30.0
    while pow(s,0.5)/pow(i, 0.5) > 0.1:
        i += 1
        x = nor_est3()
        a = m
        m = m + (x - m)/i
        s = (1 - 1.0/(i - 1))*s + i*((m - a)**2)
    return (i, m, s)

N = 10**4
suma = 0.0
s1 = 0.0
s2 = 0.0
for i in range(N):
    a,b,c= ej1()
    suma = suma + a
print "Esperanza", suma/N
print "media: ", b
print "varianza: ", c
