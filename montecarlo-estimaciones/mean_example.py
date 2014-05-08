from random import random
from math import e, floor

def foo(k):
    s = 0.0
    for j in range(0,k):
        u = random()
        x = (floor(10000*u) + 1)/10000
        s += pow(e, x)
    return s*10**4/k

print foo(100)
