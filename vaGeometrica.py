from random import random
from math import log


def geometric(p):
    u = random()
    q = 1 - p
    x = int(log(u)/log(q)) + 1
    return x


for i in range(20):
    p = random()
    print geometric(0.4)
