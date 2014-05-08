from random import random
def get_u2():
    y=random()
    return foo(((1/y)-1))/y**2
def foo(x):
    return x*pow((1+x**2),-2)
b=0.0
n=10**6
for i in range(0,n):
    b+=get_u2()/float(n)
print b
