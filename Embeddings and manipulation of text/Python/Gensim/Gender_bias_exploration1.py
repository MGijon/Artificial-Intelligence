import numpy as np
import pandas as pd
import gensim.models as gm
import matplotlib.pyplot as plt
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

## Builting synsets
## ================


total_size = len(model.wv.vocab)

## Threshold and loops
## ===================
threshold = 0.25
logger.info('Threshold fixed at %s\n', threshold)


## Statistics
## ==========


## Graphic representation
## ======================

#print(model.most_similar( positive = ['woman', 'doctor'], negative = ['man'], topn = 1))
