from random import random
from math import log10

def gamma(l, n):
    acc = 1.0
    for i in range(n):
        acc *= random()
    return (-1.0/l)*log10(acc)


for i in range(10):
    print gamma(3, 10)
