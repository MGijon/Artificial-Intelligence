import gensim.models as gm
import numpy as np

sentences = [['first', 'sentence'], ['second', 'sentence']]

# train the model on the two sentences
model = gm.Word2Vec(sentences, min_count = 1)  # default value for min_count is 5

print(type(model.wv['first']))              # <class 'numpy.ndarray'>, arrays shape = (100,)


# Construct a list to save the words
list_words_embedded = []

for sentence in sentences:
    for word in sentence:
        list_words_embedded.append(model.wv[word])

print(type(list_words_embedded))
print(len(list_words_embedded))             # 4     -> here is the problem, the duplicity of words
print(type(list_words_embedded[0]))         # <class 'numpy.ndarray'>

# To solve this a set of the words will be create
 # first create a lis of the words using the previous loop

list_words = []
for sentence in sentences:
    for word in sentence:
        list_words.append(word)

 # now we create a set from this list

set_words = set(list_words)
print(set_words)                           # has no repeated words

# now we recosntruc the list of embeded words

list_words_embedded_clean = []

for w in set_words:
    list_words_embedded_clean.append(model.wv[w])

print(type(list_words_embedded_clean))
print(len(list_words_embedded_clean))             # 4     -> here is the problem, the duplicity of words
print(type(list_words_embedded_clean[0]))         # <class 'numpy.ndarray'>
