import gensim.models as gm
import pandas as pd

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
#route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

def back_fort(word):
    '''
    Devuelve una tupla: palabra, distancia
    '''
    resultado = model.most_similar(positive = ['women', word], negative = ['men'])
    resultado = model.most_similar(positive = ['men', resultado[0][0]], negative = ['women'])

    return resultado[0]

vocabulario = model.
