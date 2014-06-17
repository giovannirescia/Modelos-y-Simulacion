from random import random
import math
import numpy as np

def server():
    l1 = 4.0
    l2 = 4.2
    t = 0
    i = 0
    repairs = {}
    arrivals = {}
    time_on_system = 0.0
    more_arrivals = True
    exp = lambda x: (-1.0 / x) * math.log(random())
    while True:
        new_arrival = t + exp(l1)
        if repairs:
            min_key = min(repairs, key=repairs.get)
            repair_time = repairs[min_key]
        else:
            repair_time = float("inf")
        if more_arrivals and new_arrival < repair_time:
            if t + new_arrival > 8:
                more_arrivals = False
            if more_arrivals and len(repairs) <= 3:
                i += 1
                t += new_arrival
                arrivals[i] = t
                repairs[i] = t + exp(l2)
        else:
            t = repair_time
            repairs.pop(min_key)
            time_on_system += repair_time - arrivals[min_key]
        if not more_arrivals and not repairs:
            break
    return [time_on_system, i]
B = 100
iters = 10000
ww = []
nn = []
for i in range(iters):
    [w, n] = server()
    ww.append(w)
    nn.append(n)
d_ = np.mean(ww)
n_ = np.mean(nn)
mean = d_ / n_
print "Tiempo promedio que un cliente pasa en el sistema %f" % mean
ecm = 0.0
for _ in range(B):
    d = 0.0
    n = 0.0
    for _ in range(iters):
        I = int(random() * iters)
        d += ww[I]
        n += nn[I]
    ecm += (d / n - mean) ** 2
ecm /= B
print "El error cuadratico medio del estimador es %f\n" % ecm
