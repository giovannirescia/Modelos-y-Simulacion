from generalized_integrals import *
def f(x):
    return 1/(x**3+1)

a=0.0
for i in range(0,10**6):
    a+=minus_infinity_to_infinity(f)/10**6

print a
