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
    Llena las lista con la info de la palabra que le pasemos.
    '''
    Word.append(word)
    Word_vector.append(model.word_vec(word))

    back = model.most_similar(positive = ['women', word], negative = ['men'])
    fort = model.most_similar(positive = ['men', back[0][0]], negative = ['women'])

    Back_resoult.append(back[0][0])
    Back_vector.append(model.word_vec(back[0][0]))
    Back_distance.append(back[0][1])

    Fort_resoult.append(fort[0][0])
    Fort_vector.append(model.word_vec(fort[0][0]))
    Fort_distance.append(fort[0][1])

test_list = ['king', 'computer', 'work', 'kind', 'house', 'dog']

for i in test_list:
    back_fort(i)

df = pd.DataFrame()
df['Word'] = Word
df['Word_vector'] = Word_vector
df['Back_resoult'] = Back_resoult
df['Back_vector'] = Back_vector
df['Back_distance'] = Back_distance
df['Fort_resoult'] = Fort_resoult
df['Fort_vector'] = Fort_vector
df['Fort_distance'] = Fort_distance

import pickle as pk

pk.dump(df, open('Data/Concept_proof6.p', 'wb')) # the file is now created

# df_recuperado = pk.load(open('Data/Concept_proof6.p', 'rb'))
