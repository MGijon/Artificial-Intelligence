import gensim.models as gm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
#route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

words = list(model.vocab.keys())[:1000]

data = pd.DataFrame()
data['words'] = words
data['values'] = [model.most_similar( positive = ['women', i],
                  negative = ['men'], topn = 1)[0][1] for i in data['words']]

data.to_csv('Data/Concept_proof.csv', index = False)

####################################

datos = pd.read_csv('Data/Concept_proof.csv')
valores = datos['values']
len(valores)

# hacemos una primera visualización de los datos mediante un simple histograma
plt.figure(figsize = (10, 7.5))
plt.xlabel('Distancias por la relación de género')
plt.ylabel('Número de muestras')
plt.title('Gender bias 1000 first words')
valores.plot(kind = 'hist', bins = 50)
plt.savefig('Data/1000_words_histogram.png')
plt.show()
