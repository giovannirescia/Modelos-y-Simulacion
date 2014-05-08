from random import random
from math import sqrt, log10

def transfinv(f):
    u = random()
    return f(u)

#example -x/2 + 1
def foo(x):
    return 2 + 2*(sqrt(x))


#example 1 - e**-x
def expo(x):
    return -log10(x)

#example x**n

def example(x):
    return pow(x, 1/10.0)

#example x**n
def example2(n):
    l=[]
    for i in range(n):
        l.append(random())
    l.sort(reverse = True)
    return l[0]

for i in range(5):
    print example2(10)


