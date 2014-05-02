from random import random
from math import log10


def geometric(p):
    u = random()
    q = 1 - p
    x = int(log10(u)/log10(q)) + 1
    return x


for i in range(20):
    p = random()
    print geometric(0.4)
