from random import random
from math import e
def foo_c(x):
    return e**(-(x**2))

def get_u2():
    y=random()
    return foo_c(1/y-1)/pow(y,2)

n=10**6
b=0.0
for i in range(0,n):
    b+=2*get_u2()/n
print b
