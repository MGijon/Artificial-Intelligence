import numpy as np
import pandas as pd
import gensim.models as gm
import matplotlib.pyplot as plt
import seaborn as sn
from nltk.corpus import wordnet as wn

route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

result = model.most_similar(positive = ['women', 'king'], negative = ['men'], topn = 1)

result[0][0]
