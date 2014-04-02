from math import e
from random import random

def get_max():
    s=random()
    n=1
    while s>=e**(-3):
        s*=random()
        n+=1
    return n-1

def estimation(n):
    estimations=0.0
    for i in range(0,n):
        estimations+=get_max()
    print estimations/float(n)

N=[10*2,10**3,10**4,10**5,10**6]

print "PARTE A)\r\n"
for i in N:
    estimation(i)

print "\r\nPARTE B)\r\n"
def probabily(i,n):
    hits=0
    for k in range(0,n):
        if i==get_max():
            hits+=1
    print hits/float(n)

for i in range(0,7):
    probabily(i,10**6)
