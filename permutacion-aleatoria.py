from random import random

def assoc_list(l1, l2):
    res = []
    for i in range(0, len(l1)):
        res.append((l1[i], l2[i]))
    return res


def permutacion(nset):

    k = len(nset) - 1
    while k > 0:
        u = random()
        l = int(u*k)+1
        aux_1, aux_2 = nset.index(nset[k]), nset.index(nset[l])
        nset[aux_1], nset[aux_2] = nset[aux_2], nset[aux_1]
        k -= 1

    return nset


def perms2(nset):
    uniforms_list = [random() for i in range(0, len(nset)-1)]
    l = assoc_list(uniforms_list, nset)
    l.sort()
    res = []
    for i in l:
        res.append(i[1])
    return res


nset = ['a', 'b', 'c', 'd', 'e']

#for i in range (0,20):
#    print permutacion(nset)

for i in range(0, 20):
    print perms2(nset)
