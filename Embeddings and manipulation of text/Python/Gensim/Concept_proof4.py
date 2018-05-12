import gensim.models as gm
import pandas as pd

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
#route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

print(model.vocab['Hello'])
def back_fort(word):
    '''
    Devuelve una tupla: palabra, distancia
    '''
    resultado1 = model.most_similar(positive = ['women', word], negative = ['men'])
    resultado2 = model.most_similar(positive = ['men', resultado1[0][0]], negative = ['women'])

    return (word, resultado1[0][0], resultado1[0][1],
            resultado2[0][0], resultado2[0][1])

vocabulario = list(model.vocab)

len(vocabulario)

for v in vocabulario[0:10]:
    print(back_fort(v))
