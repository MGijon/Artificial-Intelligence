import numpy as np
import pandas as pd
import gensim.models as gm
import matplotlib.pyplot as plt
import seaborn as sn
import logging
from nltk.corpus import wordnet as wn

## Logging
## =======

# create logger
logger = logging.getLogger('report_Gender_bias_debiation')
logger.setLevel(logging.DEBUG)
# create file handler
fh = logging.FileHandler('report_Gender_bias_debiation.log')
fh.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)

## Load the pre-trained model
## ==========================

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
# route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)
logger.info('Model loaded successfully\n')

# TENGO QUE ENCONTRAR UNA MANERA MEJOR DE DEFINIR LOS CONJUNTOS, SUPONGO QUE
# UTILIZANDO : synsets de ser vivo y artefacto: living_thing
# para cada hipónimo tendremos un cierto porcentaje de elementos que
# cuya imagen por la regularidad tiene una o más palabras a esa distancia
# por ahora eso, en el futuro ver cuántas palabras haya esa distancia

# total_size = len(model.wv.vocab) it's too big, we must select appropiate subsetes

## Builting synsets
## ================

A = wn.synsets('artifact')
A
A = wn.synset('artifact.n.01')
len(A.hyponyms())

B = wn.synsets('living_thing')
B
B = wn.synset('living_thing.n.01')
len([x.hyponyms() for x in B.hyponyms()])

C = wn.synset('dog.n.01')
len(C.hyponyms())

D = wn.synset('cat.n.01')
len(D.hyponyms())
C.hyponyms()


E = wn.synsets('dog')
E_h = []
for i in E:
    for j in i.hyponyms():
        E_h.append(j)
len(E_h)

def check_ss(word):
    T = wn.synsets(word)
    T_h = []
    for i in T:
        for j in i.hyponyms():
            T_h.append(j)
    print(len(T_h))

check_ss('cat')
check_ss('person')
check_ss('living_thing')
check_ss('artifact')
check_ss('men')
check_ss('women')
check_ss('television')
check_ss('good')
check_ss('evil')
check_ss('animal')
check_ss('dog')

def return_synsets(W):
    T = wn.synsets(W)
    T_h = []
    for i in T:
        for j in i.hyponyms():
            T_h.append(j)
    return T_h

return_synsets('cat')

def return_synsets_2_levels(W):
    T = return_synsets(W)
    T_h = T
    for i in T:
        for j in i.hyponyms():
            T_h.append(j)
    return T_h

len(return_synsets_2_levels('cat'))

def return_synsets_3_levels(W):
    T = return_synsets_2_levels(W)
    T_h = T
    for i in T:
        for j in i.hyponyms():
            T_h.append(j)
    return T_h

len(return_synsets_3_levels('cat'))
len(return_synsets_3_levels('dog'))


## Threshold and loops
## ===================
threshold = 0.25
logger.info('Threshold fixed at %s\n', threshold)


## Statistics
## ==========


## Graphic representation
## ======================

#print(model.most_similar( positive = ['woman', 'doctor'], negative = ['man'], topn = 1))
