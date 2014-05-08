from random import random
from math import log

def weibull(a, b):
    u = random()
    t = -log(u)/a
    return pow(t, 1.0/b)

for i in range(20):
    print weibull(1,1)
