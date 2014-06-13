from math import e
from random import random
from recursive_mean_var import mean, var

def ej5():
    u1 = 2*random() - 1
    u2 = 2*random() - 1
    result = 0
    if u1**2 + u2**2 <= 1:
        result = 4
    return result

def pm(v):
    s = sum(v)
    return s/float(len(v))

#l=[ej5() for i in range(10000)]
#print pm(l)

def interval():
    l = [ej5() for j in range(30)]
    s = var(l)
    media = mean(l)
    new_mean = media
    i = float(30)
    while 2*1.96*(s/pow(i,0.5)) > 0.1:
        x = ej5()
        i += 1
        new_mean = media + (x - media)/i
        s = (1 - 1.0/(i-1))*s + i*(new_mean - media)**2
        media = new_mean
    return int(i)


n = 10**2
s = 0.0
for i in range(n):
    s += interval()
print s/n
