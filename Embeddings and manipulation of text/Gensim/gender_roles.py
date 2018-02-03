import gensim.models as gm
import numpy as np

model = gm.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary = True)

print(model.most_similar( positive = ['woman', 'doctor'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'champion'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'hero'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'director'], negative = ['man'], topn = 1))
