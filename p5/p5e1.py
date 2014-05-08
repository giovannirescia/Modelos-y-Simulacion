from random import random, seed

def f1():

    u = random()
    if u <= 0.25:
        return 2*(1 + pow(u,0.5))
    else:
        return 6*(1 - pow((1-u)/3, 0.5))


for i in range(20):
    print f1()
