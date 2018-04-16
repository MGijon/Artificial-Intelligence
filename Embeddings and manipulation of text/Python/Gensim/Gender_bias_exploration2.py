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
BALL_small = BALL_small[0:100]

distancias = []

result = model.most_similar(positive = ['women', 'king'], negative = ['men'], topn = 1)

result[0][0]
