import gensim.models as gm
import numpy as np

sentences = [['first', 'sentence'], ['second', 'sentence']]
# train the model on the two sentences
model = gm.Word2Vec(sentences, min_count = 1)  # default value for min_count is 5


#print(model.wv['first'])                    # [  4.26240359e-03  -3.45680979e-03  ...  -1.74149941e-03]
print(type(model.wv['first']))              # <class 'numpy.ndarray'>
print(model.wv['first'].shape)              # (100,)

# Construct a list to save the words
list_words = [[[word for word in sentence] for sentence in sentences]]
print(list_words)
print(type(list_words))                     # <class 'list'>

list_words_embedded = matrix = [[[model.wv[word] for word in sentence] for sentence in sentences]]
print(len(list_words_embedded))