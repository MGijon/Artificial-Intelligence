import gensim.models as gm
import numpy as np
import pandas as pd

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
#route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

data = pd.DataFrame()
data['WORDS'] = list(model.vocab.keys())

data.to_csv('Data/Model_Vocabulary.csv', sep = ';', index = False)

data1 = pd.DataFrame()
data1['WORDS'] = list(model.vocab.keys())[:500000]
data1.to_csv('Data/Model_Vocabulary_part1.csv', sep = ';', index = False)

data2 = pd.DataFrame()
data2['WORDS'] = list(model.vocab.keys())[500000:1000000]
data2.to_csv('Data/Model_Vocabulary_part2.csv', sep = ';', index = False)

data3 = pd.DataFrame()
data3['WORDS'] = list(model.vocab.keys())[1000000:1500000]
data3.to_csv('Data/Model_Vocabulary_part3.csv', sep = ';', index = False)

data4 = pd.DataFrame()
data4['WORDS'] = list(model.vocab.keys())[1500000:2000000]
data4.to_csv('Data/Model_Vocabulary_part4.csv', sep = ';', index = False)

data5 = pd.DataFrame()
data5['WORDS'] = list(model.vocab.keys())[2500000:]
data5.to_csv('Data/Model_Vocabulary_part5.csv', sep = ';', index = False)
