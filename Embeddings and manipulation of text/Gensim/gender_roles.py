import gensim.models as gm
import numpy as np

route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

print(model.most_similar( positive = ['woman', 'doctor'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'champion'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'hero'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'director'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'throne'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'winner'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'power'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'control'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'leader'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'wise'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'intelligent'], negative = ['man'], topn = 1))
print(model.most_similar( positive = ['woman', 'clever'], negative = ['man'], topn = 1))
