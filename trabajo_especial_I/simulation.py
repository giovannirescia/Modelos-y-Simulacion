from random import random, seed
from math import e, log


def exp(l):
    u = random()
    return log(u)*(-1.0/l)


def simulation():
    working_machines = 5
    spare_machines = 2
    system_failure = False
    # T_f = media tiempo de falla de una maquina = 1 mes
    # T_r = media tiempo de reparacion de una maquina = 1/8
    # broken_machines = system state, numero de maquinas rotas en el tiempo t
    t = 0
    broken_machines = 0
    machine_repair_time = float("inf")
    l = [exp(1) for i in range(working_machines)]
    l.sort()
    while not system_failure:
        # la primer maquina falla antes que se termine el arreglo de otra
        if l[0] < machine_repair_time:
            t = l[0]
            broken_machines += 1
            # mas maquinas rotas que maquinas de repuesto, falla del sistema
            if broken_machines > spare_machines:
                T = t
                system_failure = True
            # si hay maquinas de repuesto, averiguo cuanto dura
            elif broken_machines <= spare_machines:
                x = exp(1)
                l.pop(0)
                l.append(x+t)
                l.sort()
            # si hay una maquina rota, la reparo, y tardo y + t
            if broken_machines == 1:
                y = exp(8)
                machine_repair_time = t + y
        # sin fallo antes que la maquina sea reparada
        elif machine_repair_time <= l[0]:
            t = machine_repair_time
            broken_machines -= 1
            if broken_machines > 0:
                y = exp(8)
                machine_repair_time = t + y
            elif broken_machines == 0:
                machine_repair_time = float("inf")

    return T

N = [10**i for i in range(2, 5)]


def esperanza(N):
    media = 0.0
    for i in range(N):
        media += simulation()
    return media/N


def varianza(N):
    media = esperanza(N)
    varianza = 0.0
    for _ in range(N):
        varianza += (simulation() - media)**2
    return varianza/(N-1)


for i in N:
    print "\r\nSimulacion con dos operarios\r\n"
    print "Esperanza:             ", repr(round(esperanza(i), 3))
    print "Varianza:              ", repr(round(varianza(i), 3))
    print "Desviacion Estandar:   ", repr(round(varianza(i)**0.5, 3))
    print "\r\n"
