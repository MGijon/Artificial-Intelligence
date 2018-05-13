import gensim.models as gm
import pandas as pd
import numpy as np

route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

def back_fort(word):
    '''
    Devuelve una tupla: palabra, distancia
    '''
    back = model.most_similar(positive = ['women', word], negative = ['men'])
    fort = model.most_similar(positive = ['men', back[0][0]], negative = ['women'])
    #count = model.vocab[word][0]
    #index = model.vocab[word][1]
    word_vector = model.word_vec(word)
    back_vector = model.word_vec(back[0][0])
    fort_vector = model.word_vec(fort[0][0])

    return (word, word_vector, back[0][0], back_vector, back[0][1],
            fort[0][0], fort_vector, fort[0][1])

test_list = ['king', 'computer', 'work', 'kind', 'house', 'dog']

df = pd.DataFrame()
df['Word'] = []
df['Word_vector'] = []
df['Back_resoult'] = []
df['Back_vector'] = []
df['Back_distance'] = []
df['Fort_resoult'] = []
df['Fort_vector'] = []
df['Fort_distance'] = []

Word = []
Word_vector= []
Back_resoult = []
Back_vector = []
Back_distance = []
Fort_resoult = []
Fort_vector = []
Fort_distance = []

for w in test_list:
    aux = back_fort(w)
    Word.append(aux[0])
    Word_vector.append(aux[1])
    Back_resoult.append(aux[2])
    Back_vector.append(aux[3])
    Back_distance.append(aux[4])
    Fort_resoult.append(aux[5])
    Fort_vector.append(aux[6])
    Fort_distance.append(aux[7])

df['Word'] = Word
df['Word_vector'] = Word_vector
df['Back_resoult'] = Back_resoult
df['Back_vector'] = Back_vector
df['Back_distance'] = Back_distance
df['Fort_resoult'] = Fort_resoult
df['Fort_vector'] = Fort_vector
df['Fort_distance'] = Fort_distance

df.to_csv('Data/Concept_proof4_1')
