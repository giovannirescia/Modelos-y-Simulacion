def mean(values):
    result = 0.0
    n = 0.0
    for x in values:
        n += 1
        delta = x - result
        result = result + delta/n
    return result

def var(values):
    n = 0
    mean = 0
    M2 = 0
 
    for x in values:
        n = n + 1
        delta = x - mean
        mean = mean + delta/n
        M2 = M2 + delta*(x - mean)
 
    variance = M2/(n - 1)
    return variance

########### EJEMPLOS DE PRUEBA ###########


#val2 =[round(2*n-n**0.5 +1,3) for n in range(30)]
#print val2
#media= mean(val2,8)
#print var(val2)

