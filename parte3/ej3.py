from random import random
from math import e
from recursive_mean_var import mean, var

def ej3():
    acc = random()
    sum = acc
    iter = 1
    while sum <= 1:
        sum += random()
        iter += 1
    return iter

def exp():
    N = 10**3
    s = 0.0
    for i in range(N):
        s += ej3()
    return s/N  
###### ERROR CUADRATICO MEDIO ########

#a = 0.0
#var = 0.0
#for i in range(1000):
#    a = exp()
#    var = (a - e)**2
#print var/1000
####################################

def interval():
    l = [ej3() for j in range(30)]
    s = var(l)
    media = mean(l)
    new_mean = media
    i = float(30)
    while 2*1.96*(s/pow(i,0.5)) > 0.01:
        x = ej3()
        i += 1
        new_mean = media + (x - media)/i
        s = (1 - 1.0/(i-1))*s + i*(new_mean - media)**2
        media = new_mean
    return (new_mean - 1.96*(s/pow(i,0.5)), new_mean + 1.96*(s/pow(i,0.5)))

print interval()
