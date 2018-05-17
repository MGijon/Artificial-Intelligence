import pandas as pd
import gensim.models as gm
import scipy.spatial.distance as distance

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
Cosine_back = []
Cosine_fort = []

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

test_list = ['king']

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

len(Word_vector[0])
len(Back_vector[0])

for i in range(0, len(Word_vector)):
    Cosine_back.append(distance.cosine(Word_vector[i], Back_vector[i]))
    Cosine_fort.append(distance.cosine(Word_vector[i], Fort_vector[i]))

distance.cosine(Word_vector[0], Back_vector[0])
distance.cosine(Word_vector[0], Fort_vector[0])

df['Cosine_back'] = Cosine_back
df['Cosine_fort'] = Cosine_fort


import pickle as pk

pk.dump(df, open('Data/Concept_proof7.p', 'wb')) # the file is now created

# test
df_recuperado = pk.load(open('Data/Concept_proof7.p', 'rb'))

df_recuperado.head()
