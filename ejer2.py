from generalized_integrals import *
from tabulate import tabulate
from math import e

def integral_2a(x):
    return (1-x**2)**1.5


def integral_2b(x):
    return x*(1+x**2)**(-2)


def integral_2c(x):
    return e**-(x**2)


def integral_2d(x, y):
    return e**((x+y)**2)


def integral_2e(x, y):
    return e**(-(x+y))


def calc_integral(integral,i):
    c=0.0
    if integral[0]==a_to_b:
        for j in range(0,i):
            c+=integral[0](integral[1],integral[2],integral[3])/i
    else:
        for j in range(0,i):
            c+=integral[0](integral[1])/i
    return c

integrals_list=[(a_to_b,integral_2a,0,1),
                (zero_to_infinity,integral_2b),
                (minus_infinity_to_infinity,integral_2c),
                (multiple_integral_zero_to_one,integral_2d),
                (multiple_integral_zero_to_infinity,integral_2e)]

table = []
headers = ['N','a)','b)','c)','d)','e)']
N = [10**i for i in range(2, 7)]

for n in N:
    table.append([n])

for integral in integrals_list:
    k=0
    for n in N:
        c=calc_integral(integral,n)
        table[k].append(c)
        k+=1

print tabulate(table, headers, tablefmt="orgtbl")
