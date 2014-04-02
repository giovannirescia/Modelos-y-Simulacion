from random import random
from tabulate import tabulate


def get_min():
    s=0.0
    n=0
    while s<1.0:
        s+=random()
        n+=1
    return n

def estimation(n,f):
    estimations=0.0
    for i in range(0,n):
        estimations+=f()
    return estimations/float(n)

N=[10**2,10**3,10**4,10**5,10**6]
table=[]
k=0
headers=['N', 'E(N)']
for n in N:
    table.append([n])
for i in N:
    table[k].append(estimation(i,get_min))
    k +=1
print tabulate(table, headers, tablefmt="orgtbl")
