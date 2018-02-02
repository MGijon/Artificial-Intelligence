import gensim.models as gm
import numpy as np

model = gm.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary = True)

print(model.most_similar( positive = ['woman', 'king'], negative = ['man'], topn = 1))
