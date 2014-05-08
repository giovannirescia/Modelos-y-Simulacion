from random import random
from tabulate import tabulate
from estimation import estimation

def get_min():
    s=0.0
    n=0
    while s<1.0:
        s+=random()
        n+=1
    return n


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
