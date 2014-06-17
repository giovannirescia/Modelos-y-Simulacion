from math import e
from random import random

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


def interval():
    x = ej5()
    m = x
    s = 0.0
    for i in range(2,31):
        x = ej5()
        a = m
        m = m + (x - m)/float(i)
        s = (1 - 1/(float(i)-1))*s + i*(m -a)**2
    i = 30.0

    while 2*1.96*(pow(s/i,0.5)) > 0.1:
        i += 1
        x = ej5()
        a = m
        m = m + (x - m)/float(i)
        s = (1 - 1/(float(i)-1))*s + i*(m -a)**2
    return i


n = 10**2
s = 0.0
for i in range(n):
    s += interval()
print s/n
