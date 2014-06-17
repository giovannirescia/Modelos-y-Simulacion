from random import random


def g(f,a,b):
    return f(a + (b-a) * random()) * (b - a)

def f(x):
    return x**2


def ex(a,b):
    x = g(f,a,b)
    m = x
    s = 0
    for i in range(2,101):
        x = g(f,a,b)
        w = m
        m = m + (x - m)/float(i)
        s = (1 - 1/(float(i)-1))*s + i*(m-w)**2
    i = 102.0
    while 1.96*pow(s/i,0.5) > 0.005:
        i += 1
        x = g(f,a,b)
        w = m
        m = m + (x - m)/i
        s = (1 - 1.0/(i - 1))*s + i*((m - w)**2)

    return (i, m, s)

a=0
b=2
print ex(a,b)
