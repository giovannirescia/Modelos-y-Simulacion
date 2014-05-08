from math import pi, sin
from random import random

def intersect():
    r=2*random()
    angle=pi*random()
    y_a=r+0.5*sin(angle)
    y_b=r-0.5*sin(angle)

    if y_a>=2 or y_b<=0:
        n=1
    else:
        n=0
    return n

def simulation(n):
    hits=0
    for i in range(0,n):
        if intersect():
            hits+=1
    print pow(hits/float(n),-1)

N=[10**3,10**4,10**5]
for i in N:
    simulation(i)
