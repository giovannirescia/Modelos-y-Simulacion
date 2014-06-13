from vanormal import normal_estandar
from recursive_mean_var import mean, var
from random import random

def ej1():

    lista_normales = [random() for j in range(30000)]
    media = mean(lista_normales)
    s = var(lista_normales)
    i = float(len(lista_normales))
    new_mean = media
    while s/pow(i,0.5) >= 0.1:
        x = normal_estandar()
        i += 1
        new_mean = media + (x - media)/i
        s = (1 - 1.0/(i-1))*s + i*(new_mean - media)**2
        media = new_mean
    return (i, new_mean, s)

N = 10**0
suma = 0.0
for i in range(N):
    a,b,c= ej1()
    suma = suma + a
print "Esperanza", suma/N
print "numero de datos: ", a
print "media: ", b
print "varianza: ", c
