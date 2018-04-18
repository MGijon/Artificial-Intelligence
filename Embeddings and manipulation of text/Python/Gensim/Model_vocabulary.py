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

data.to_csv('Data/Model_Vocabulary', sep = ';', index = False)
