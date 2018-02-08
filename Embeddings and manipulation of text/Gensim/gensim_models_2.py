import numpy as np
import gensim.models as gm

# sentences : The Room (2003)
sentences = [['Hi', 'doggy'],
             ['Oh', 'actually', 'Johnny', 'I', 'got', 'a', 'I', 'got', 'a', 'little', 'bit', 'of', 'a', 'tragedy'],
             ['You', 'are', 'tearing', 'me', 'apart', 'Lisa'],
             ['Thank', 'you', 'honey', 'this', 'is', 'a', 'beautiful', 'party'],
             ['You', 'invited', 'all', 'my', 'friends', 'good', 'thinking'],
             ['All', 'men', 'are', 'assholes'],
             ['Men', 'and', 'women', 'use', 'and', 'abuse', 'each', 'other', 'all', 'the', 'time', 'there', 'is',
              'nothing', 'wrong', 'with', 'it'],
             ['Marriage', 'has', 'nothing', 'to', 'do', 'with', 'love']]
# create a list:
list_words = []
for sentence in sentences:
    for word in sentence:
        list_words.append(word)

#print(len(list_words))                          # 65
# i'll clean it turning into a set

set_words = set(list_words)

# i'll create from this a clean list of non-repeat words
list_words = [w for w in set_words]

#print(len(list_words))                          # 53

####################################################################################

# Now we select and train a model to get the matrix of embeddings of this set of words
model = gm.Word2Vec(sentences, min_count = 1)

embeded_words_list = [model.wv[word] for word in list_words] # list with the embeddings of the words

# try to get now a numpy matrix to manipulate better the data:

matrix_embedings = np.matrix([range(0, len(list_words))], [range(0, 10)])   # ARREGLARLO !!
print(matrix_embedings)
