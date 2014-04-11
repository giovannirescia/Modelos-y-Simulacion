from random import random

def inverse_transform(probabilities):

    probabilities.sort()
    u = random()
    i = 0
    x = 0
    done = False
    while not done:
        if u < probabilities[i]:
            x = i
            done = True
        else:
            i+=1
        if i==len(probabilities):
            x = i
            done = True
    return x


prob =  [0.6, 0.15, 0.1, 0.05, 0.05, 0.05]

for i in range(0,20):
    print inverse_transform(prob)
