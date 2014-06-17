from random import random

def ej4():
    u1 = random()
    u2 = random()
    i = 2
    while u1 < u2:
        i += 1
        u1 = u2
        u2 = random()
    return i

s = 0.0
N = 10**3
for i in range(N):
    s += ej4()
print s/N
