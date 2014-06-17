from __future__ import division
from random import random
from scipy import stats


def prob_mass_funct(p):
    return [stats.binom.pmf(x, 8, p) for x in range(0,9)]

def gen_p_estim(sample_list, n):
    return (sum(sample_list)/len(sample_list))/8

# calculo de t
def estadistico_t(freq_list, p_list, m):

    t = 0.0
    for i in range(len(p_list)):
        a = (freq_list[i] - m*(p_list[i]))**2
        b = m*p_list[i]
        t += a/b
    return t

n = 8
obs = [6,7,3,4,7,3,7,2,6,3,7,8,2,1,3,5,8,7]
p_est = gen_p_estim(obs, n)

freq = []
for j in range(0,9):
    freq.append(obs.count(j))

# lista de las probabildades p_i
p_list = prob_mass_funct(p_est)


m = len(obs)
t = estadistico_t(freq, p_list, m)


def freq(l):
    f = []
    for j in range(0,9):
        f.append(l.count(j))
    return f


print ("\r\nSimulacion \r\n")
r = 1000
hits = 0
print p_est
for i in range(r):

    val_array = stats.binom.rvs(8, p_est, size=m)
    val_list = list(val_array)
    val_freq = freq(val_list)
    p = gen_p_estim(val_list, n)
    p_list = prob_mass_funct(p)

    T = estadistico_t(val_freq, p_list, m)
    if T >= t:
        hits += 1

print hits/r
