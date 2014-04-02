from math import e
from random import random

def integral(x):
    return e**-(x)
def aux(x,y):
    if y<x:
        return 1
    else:
        return 0
def integrate():
    x=random()
    y=random()
    if y<x:
        r=(integral(1/x -1)/x**2)*(integral(1/y -1)/y**2)
    else:
        r=0
    return r
N=[10**i for i in range(3,7)]
c=0.0
def for_each(n):
    c=0.0
    for i in range(0,n):
        c+=integrate()/n
    return c


for i in N:
    c=for_each(i)
    print repr(c) + "     -----------------    " + repr(i)

