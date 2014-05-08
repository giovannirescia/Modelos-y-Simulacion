from random import random
from math import e, log, pi, sin, cos


# f(x) = 2/(2pi)**0.5 * e(-x**2 / 2)
# g(x) = E(1)
# c = (2e/pi) ** 0.5


#Normal a partir de una exponencial ~(1)
def normal_estandar():
    u = random()
    v = random()
    y = -log(u)
    aux = pow(y - 1, 2)
    exp = pow(e, -aux/2.0)
    while v > exp:
        u = random()
        v = random()
        y = -log(u)
        aux = pow(y - 1, 2)
        exp = pow(e, -aux/2.0)
    return y

#Normal a partir de dos exponenciales ~(1)
def nor_est2():
    u = random()
    v = random()
    y1 = -log(u)
    y2 = -log(v)
    while y2 < pow((y1 -1),2) / 2.0:
        u = random()
        v = random()
        y1 = -log(u)
        y2 = -log(v)
    return y1

#Normal estandar y exponencial ~(1)
def nor_est3():
    u = random()
    v = random()
    y1 = -log(u)
    y2 = -log(v)
    aux_y = y2 -((y1-1)**2)/2.0
    while 0 >= aux_y:
        u = random()
        v = random()
        y1 = -log(u)
        y2 = -log(v)
        aux_y = y2 -((y1-1)**2)/2.0
    t = random()
    if t < 0.5:
        z = y1
    else:
        z = -y1
    return z

#Normales estandar por metodo polar

def polar():
    u1 = random()
    u2 = random()
    r = -2*log(u1)
    o = 2*pi*u2

    x = (r**0.5)*cos(o)
    y = (r**0.5)*sin(o)

    return (x, y)

#Normales estandar por metodo polar optimizado

def polar2():
    u1 = random()
    u2 = random()
    v1 = 2*u1 - 1
    v2 = 2*u2 - 1
    s = v1**2 + v2**2
    while s >= 1:
        u1 = random()
        u2 = random()
        v1 = 2*u1 - 1
        v2 = 2*u2 - 1
        s = v1**2 + v2**2

    x = pow(-2*log(s)/s, 0.5)*v1
    y = pow(-2*log(s)/s, 0.5)*v2

    return (x, y)





print "PRIMER METODO POLAR\r\n\r\n"
for i in range(15):
    print polar()


print "\r\n\r\nSEGUNDO METODO POLAR\r\n\r\n"
for i in range(15):
    print polar2()


#print "PRIMER METODO\r\n\r\n"

#for i in range(5):
#    print normal_estandar()

#    print "\r\n\r\nSEGUNDO METODO\r\n\r\n"

#for i in range(5):
#    print nor_est2()

#print "\r\n\r\nTERCER METODO\r\n\r\n"

#for i in range(6):
#    print nor_est3()
