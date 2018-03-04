import gensim.models as gm
import pandas as pd
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

# ruta mac:
filepath = 'Data/words_source_v2.2.csv'
# ruta windows:
# filepath = ''
data = pd.read_csv(filepath, sep = ';')
data.head()

data = data[['Pos1', 'R1', 'R2', 'R3', 'R4', 'R5']]

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
# route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)


#data.iloc[0]['R1']
list_words_POS1 = []
list_words_R1 = []
list_words_R2 = []
list_words_R3 = []
list_words_R4 = []
list_words_R5 = []

# aquí añadimos a la lista de palabras los elementos en la posición 1
i = 0
while isinstance(data['Pos1'][i] , str):
    list_words_POS1.append(data.iloc[i]['Pos1'])
    list_words_R1.append(data.iloc[i]['R1'])
    list_words_R2.append(data.iloc[i]['R2'])
    list_words_R3.append(data.iloc[i]['R3'])
    list_words_R4.append(data.iloc[i]['R4'])
    list_words_R5.append(data.iloc[i]['R5'])
    i += 1


def construct_word_dict(list):
    ''' Construimos un diccionario en el formato que necesitamos para el PCA '''
    dict = {}
    for i in list:
        dict[i] = model.wv.vocab[i]
    return dict


'''
for i in words:

    words_list = [list_words[0][0], ]

    words_dict = construct_word_dict(words_list)


X = model[words_dict]
pca = PCA(n_components = 2)
result = pca.fit_transform(X)


plt.scatter(result[:, 0][:2], result[:, 1][:2], c = 'green', label = 'Word')
plt.scatter(result[:, 0][2:], result[:, 1][2:], c = 'red', label = 'Resoults')
words = list(words_dict)
for i, word in enumerate(words):
	print(i, word)
	plt.annotate(word, xy = (result[i, 0], result[i, 1]))
plt.legend()
plt.show()
'''
