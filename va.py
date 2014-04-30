from random import random

def inv_transf(probs):

    probs.sort()
    u = random()
    i = 0
    x = 0
    done = False
    n = len(probs)
    my_sum = 0.0
    while not done:
        my_sum+=probs[i][1]
        if u < my_sum:
            x = probs[i][0]
            done = True
        else:
            i+=1
        if i==n:
            x = probs[i-1][0]
            done = True
    return x


#Same algorithm, optimized

def inv_transf_opt(probs):

    probs.sort(key=lambda t:t[1],reverse=True)
    u = random()
    i = 1
    x = 0
    done = False
    my_sum = 0.0
    n = len(probs)
    while not done:
        my_sum+=probs[i][1]            
        if u < my_sum:
            x = probs[i][0]
            done = True
        else:
            i+=1
        if i==n:
            x = probs[i-1][0]
            done = True
    return x



#Example


probs =  [('p1', 0.3), ('p3', 0.3), ('p4', 0.25), ('p2', 0.1), ('p0', 0.05)]
for i in range(0,20):
    print inv_transf_opt(probs)
