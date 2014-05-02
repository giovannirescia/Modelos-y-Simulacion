from random import random


def reject_method(x, y, c):
    
    j = simular(y)
    u = random()
    p_j = x(j)
    while u >= p_j/c*y(j):
        j = simular(y)
        u = random()
        p_j = x(j)
    return j
