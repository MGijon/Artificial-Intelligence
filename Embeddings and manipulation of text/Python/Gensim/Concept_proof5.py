import pandas as pd
import numpy as np
import gensim.models as gm

route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

Word = []
Word_vector= []
Back_resoult = []
Back_vector = []
Back_distance = []
Fort_resoult = []
Fort_vector = []
Fort_distance = []

def back_fort(word):
    '''
    Llena las lista con la info de la palabra que le pasemos
    '''
    Word.append(word)
    Word_vector.append(model.word_vec(word))

    back = model.most_similar(positive = ['women', word], negative = ['men'])
    fort = model.most_similar(positive = ['men', back[0][0]], negative = ['women'])

    back_vector = model.word_vec(back[0][0])
    fort_vector = model.word_vec(fort[0][0])


    Back_resoult.append(back[0][0])
    Back_vector = []
    Back_distance = []
    Fort_resoult = []
    Fort_vector = []
    Fort_distance
