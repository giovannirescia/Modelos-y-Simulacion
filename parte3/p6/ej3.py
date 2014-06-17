from random import random
from math import e
from recursive_mean_var import mean, var

def ej3():
    acc = random()
    sum = acc
    iter = 1
    while sum <= 1:
        sum += random()
        iter += 1
    return iter

def exp():
    N = 10**3
    s = 0.0
    for i in range(N):
        s += ej3()
    return s/N  


def interval():
    x = ej3()
    m = x
    s = 0
    for i in range(2,1001):
        x = ej3()
        a = m
        m = m + (x - m)/float(i)
        s = (1 - 1/(float(i)-1))*s + i*(m -a)**2

 #   i = float(30)
#    while 2*1.96*pow(s/i, 0.5) > 0.1:
  #      i += 1
   #     x = ej3()
    #    a = m
     #   m = m + (x - m)/float(i)
      #  s = (1 - 1/(float(i)-1))*s + i*(m -a)**2

    return (s, m - 1.96*(pow(s/i,0.5)), m + 1.96*(pow(s/i,0.5)))

a,b,c=interval()

print "varianza: ", a
print "intervalo: ", (b,c)


# calculo de e
#s=0.0
#for i in range(10000):
#    s += ej3()
#print s/10000
