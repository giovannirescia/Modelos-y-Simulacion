from random import random
from tabulate import tabulate


def a_to_b(f,a,b):
    x = random()
    return f(a+(b-a)*x)*(b-a)


def zero_to_infinity(f):
    x = random()
    return f(1/x-1)/x**2

#I(y)=(0,x)
def multiple_integral_zero_to_infinity(f):
    x = random()
    y = random()
    if y < x:
        return f(1/x-1, 1/y-1)/(x*y)**2
    else:
        return 0


def minus_infinity_to_zero(f):
    x = random()
    return f(-1/x + 1)/(x**2)


def minus_infinity_to_infinity(f):
    return zero_to_infinity(f)+minus_infinity_to_zero(f)


def multiple_integral_zero_to_one(f):
    x = random()
    y = random()
    return f(x, y)
