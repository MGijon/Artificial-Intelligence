import numpy as np
import pandas as pd
import gensim.models as gm
import matplotlib.pyplot as plt
import seaborn as sn
from nltk.corpus import wordnet as wn

# Cargamos el modelo:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

def numero_ramas(syn):
    '''
    Calculamos el número de hijos de cada nodo del árbol
    '''
    return len(syn.hyponyms())

conjunto = []
def recursiva(C_syn):
    '''
    Función recursiva que devuelve una lista con los hypónimos al completo.
    INPUT: conjunto de synsets (1 elemento)
    OUTPUT: lista de todos los synsets hipónimos
    '''
    for j in C_syn:
        if numero_ramas(j) == 0:
            conjunto.append(j)
        else:
            conjunto.append(j)
            for i in j.hyponyms():
                recursiva([i])
    return conjunto

SYN = wn.synsets('ball')[0]
SYN
lista = SYN.hyponyms()
BALL = recursiva([SYN])
len(BALL)

BALL = [x.lemma_names() for x in BALL]
len(BALL)

Ball = []
for i in BALL:
    for j in i:
        Ball.append(j)

Ball
distancias = []

for i in Ball:
    try:
        result = model.most_similar(positive = ['women', i], negative = ['men'], topn = 1)
        distancias.append(result[0][1])
    except KeyError:
        pass

distancias[0:10] # check the vector of distances

################################################################################

LIVING = recursiva([wn.synsets('living_thing')[0]])
len(LIVING)

LIVING = [x.lemma_names() for x in LIVING]

Living = []
for i in LIVING:
    for j in i:
        Living.append(j)

distancias = []

for i in Living[0:100]:
    try:
        result = model.most_similar(positive = ['women', i], negative = ['men'], topn = 1)
        distancias.append(result[0][1])
    except KeyError:
        pass


distancias[0:100]

################################################################################
conjunto = []
for s in wn.synsets('dog'):
    for l in s.lemmas():
        conjunto.append(l.name())
conjunto
for i in conjunto:
    try:
        result = model.most_similar(positive = ['women', i], negative = ['men'], topn = 1)
        print(result[0][1])
        distancias.append(result[0][1])
    except KeyError:
        print('no está en el vocabulario')
        pass
