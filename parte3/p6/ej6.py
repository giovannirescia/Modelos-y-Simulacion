from random import random

def ej6():
    a = [56,101,78,67,93,87,64,72,80,69]
    l = []
    for i in range(10):
        u = int(10*random())
        l.append(a[u])
    return l

def aux(li):
    return sum(li)/float(len(li))

hits = 0.0
N = 10**3
for i in range(N):
    l = ej6()
    l_prom = aux(l)
    delta = l_prom - 76.7
    if -5 < delta < 5:
        hits += 1
print hits/float(N)
