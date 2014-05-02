from random import random
from math import e, log10


def exp(l):
    u = random()
    return log10(u)*(-1.0/l)

#Exponencial a partir de Gamma

def exp2(l):
    u1 = random()
    u2 = random()
    u3 = random()
    t = (-1.0/l)*log10(u1*u2)
    X = t*u3
    Y = t - X
    print "El resultado es una tupla de dos variables exponenciales"
    return (X, Y)


# N exponenciales ~(l) a partir de Gamma ~ (l, n)

def nExp(l, n):
    acc = 1.0
    for i in range(n):
        acc *= random()
    t = (-1.0/l)*log10(acc)
    uniforms_list = []
    for i in range(n-1):
        uniforms_list.append(random())
    uniforms_list.sort()
    exp_list = []
    exp_list.append(t*uniforms_list[0])
    for i in range(0, n-2):
        exp_list.append(t*(uniforms_list[i+1]-uniforms_list[i]))
    exp_list.append(t-t*uniforms_list[-1])

    for i in exp_list: print i

nExp(3, 7)
