#La estimacion toma una cantidad de iteraciones
#y una funcion de probabilidad a la cual
#estimarle la Esperanza

def estimation(n,f):
    estimations=0.0
    for i in range(0,n):
        estimations+=f()
    return estimations/float(n)

#La probabilida toma un valor i talque
#queremos calcular P(X=i), un n
#que es la cantidad de veces que vamos
#a repetir el experimento, y una funcion
#de probabilidad 
def probability(i,n,f):
    hits=0
    for k in range(0,n):
        if i==f():
            hits+=1
    return hits/float(n)
