import numpy as np
import pandas as pd
import gensim.models as gm
import matplotlib.pyplot as plt
import seaborn as sn
from nltk.corpus import wordnet as wn

# Cargamos el modelo:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

SYN = wn.synsets('ball')[0]
lista = SYN.hyponyms()
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

BALL = recursiva([SYN])
len(BALL)

BALL_small = [x.lemma_names() for x in BALL]
BALL_small = BALL_small[0:-10]
len(BALL_small)

distancias = []

for i in BALL_small:
    try:
        POS = ['women']
        POS = POS.append(i)
        result = model.most_similar(positive = POS, negative = ['men'], topn = 1)
        distancias.append(result[0][1])
    except KeyError:
        pass


if len(set(distancias)) == 1:
    print('Hay un puto error por algún sitio')


################################################################################

LIVING = recursiva([wn.synsets('living_thing')[0]])
len(LIVING)

LIVING_small = [x.lemma_names() for x in LIVING]
LIVING_small = LIVING[0:100]
len(LIVING_small)

distancias = []

for i in LIVING_small:
    try:
        POS = ['women']
        POS = POS.append(i)
        result = model.most_similar(positive = POS, negative = ['men'], topn = 1)
        distancias.append(result[0][1])
    except KeyError:
        pass

distancias
if len(set(distancias)) == 1:
    print('Hay un puto error por algún sitio')
