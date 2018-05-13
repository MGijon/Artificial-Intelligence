import gensim.models as gm
import pandas as pd
import numpy as np

route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

def back_fort(word):
    '''
    Devuelve una tupla: palabra, distancia
    '''
    resultado1 = model.most_similar(positive = ['women', word], negative = ['men'])
    resultado2 = model.most_similar(positive = ['men', resultado1[0][0]], negative = ['women'])
    #count = model.vocab[word][0]
    #index = model.vocab[word][1]
    word_vector = model.word_vec(word)

    return (word, word_vector, resultado1[0][0], resultado1[0][1],
            resultado2[0][0], resultado2[0][1])

vocabulario = list(model.vocab)

len(vocabulario)

back_fort('home')
