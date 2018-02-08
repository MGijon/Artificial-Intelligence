import pandas as pd
import gensim.models as gm

filepath = 'Data/words_source.csv'
data = pd.read_csv(filepath, sep = ';')

data.head()

route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)


resultado = model.most_similar( positive = [data['Pos1'][0], data['Pos2'][0]],
                                negative = [data['Neg'][0]], topn = 1)

data['Resoult'][0] = resultado
data['Word'][0] = resultado[0][0]
data['Distance'][0] = resultado[0][1]

data.to_csv(filepath, sep = ';')
