import gensim.models as gm
import pandas as pd

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
#route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

words = list(model.vocab.keys())
data = pd.read_csv('Data/Concept_proof2.csv')
data['values'] = [0 for i in range(0, len(data['words']))]

for i in range(0, 1000): # rango en el que calculamos
    data['values']
data['values'] = [model.most_similar( positive = ['women', i],
                  negative = ['men'], topn = 1)[0][1] for i in data['words']]

data.to_csv('Data/Concept_proof2.csv', index = False)
