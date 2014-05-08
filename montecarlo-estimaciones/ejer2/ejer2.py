from random import random
from math import e

def get_u():
    return pow(1 -pow(random(),2),1.5)

a=0.0
for i in range(0,10**6):
    a+=get_u()
print a/float(10**6)
