import pandas as pd
import gensim.models as gm

filepath = 'Data/words_source.csv'
data = pd.read_csv(filepath, sep = ';')
data.head()

route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)


i = 0

while isinstance(data['Pos1'][i] , str):

    if isinstance(data['Word'][i] , str) == False:
        resultado = model.most_similar( positive = [data['Pos1'][i], data['Pos2'][i]],
                                        negative = [data['Neg'][i]], topn = 1)
        data['Resoult'][i] = resultado
        data['Word'][i] = resultado[0][0]
        data['Distance'][i] = resultado[0][1]

    i = i + 1

data.head()
data.to_csv(filepath, sep = ';')
