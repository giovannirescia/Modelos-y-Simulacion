from random import random
from math import e

def integrate_me(x,y):
    return e**((x+y)**2)

n=10**6
b=0.0
for i in range(0,n):
    b+=integrate_me(random(),random())/n

print b
