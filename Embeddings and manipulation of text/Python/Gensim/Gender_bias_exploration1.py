import numpy as np
import pandas as pd
import gensim.models as gm
import matplotlib.pyplot as plt

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
# route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

total_size = len(model.wv.vocab)


#print(model.most_similar( positive = ['woman', 'doctor'], negative = ['man'], topn = 1))
