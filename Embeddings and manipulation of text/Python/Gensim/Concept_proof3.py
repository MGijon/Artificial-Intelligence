import gensim.models as gm
import pandas as pd

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
#route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

words = list(model.vocab.keys())

Datos = pd.read_csv('Data/Concept_proof3.csv')
Datos.head()
palabras = Datos['words'][:10]
# no funciona todavía
Datos['value_1'] = [model.most_similar( positive = ['women', i],
                  negative = ['men'], topn = 2)[0][0][1] for i in palabras]

Datos['value_2'] = [model.most_similar( positive = ['women', i],
                  negative = ['men'], topn = 2)[1][0][1] for i in palabras]

Datos.to_csv('Data/Concept_proof3.csv', index = False)
