from math import e
from random import random
from estimation import estimation, probability

def get_max():
    s=random()
    n=1
    while s>=e**(-3):
        s*=random()
        n+=1
    return n-1

N=[10*2,10**3,10**4,10**5,10**6]

print "PARTE A)\r\n"
for i in N:
   print estimation(i,get_max)

print "\r\nPARTE B)\r\n"

for i in range(0,7):
    print probability(i,10**6,get_max)
