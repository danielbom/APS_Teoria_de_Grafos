import numpy as np
import random
import math

def sumN(vetor):
    tam = max( [len(i) for i in vetor] )
    normalizador = [0 for i in range( tam )]

    for i in vetor:
            for j in range(len(i)):
                normalizador[j] += i[j]

    return normalizador

def porcentual(vetor):
    total = sum(vetor)
    return [i/total for i in vetor]

def porcentualN(vetor):
    normalizador = [i for i in vetor]
    
    for i in range(len(vetor)):
        normalizador[i] = porcentual(normalizador[i])

    return normalizador

def porcentualNN(mat):
    tam = max( [len(i) for i in mat] )
    normalizador = [0 for i in range( tam )]

    for i in mat:
            for j in range(len(i)):
                normalizador[j] += i[j]

    return porcentual(normalizador)

def varN(vetor):
    normalizador = sumN(vetor)
    
    tam = max( [len(i) for i in vetor] )
    average_all = [ (i/len(vetor)) for i in normalizador ] # media
    sub_sqtr_all = [( (normalizador[i]-average_all[i]) ** 2 )  for i in range(len(normalizador)) ] # (x[i] - x)^2
    var_all = [ i/tam for i in sub_sqtr_all ] #  ( (x[i] - x)^2 ) / tam  

    return var_all

def dpN(vetor):
    var_all = varN(vetor) # Variancia de todos os elementos do vetor
    return [ math.sqrt(i) for i in var_all ]

def minmaxN(vetor):
    tam = max( [len(i) for i in vetor] )
    normalizador = [0 for i in range( tam )]

    for i in vetor:
            for j in range(len(i)):
                normalizador[j] += i[j]
    
    return minmax(np.array(normalizador))
    
def minmax(array_np):
    if type(array_np) == type([]):
        return minmaxN(np.array(array_np))
    return (array_np-min(array_np))/(max(array_np)-min(array_np))

def array_np(i0, iN):
    return np.array([i for i in range(i0, iN) ])

def array_np_rand(i0, iN, inter):
    x = [random.randrange(inter) for i in range(i0, iN)]
    x.sort()
    return np.array(x)