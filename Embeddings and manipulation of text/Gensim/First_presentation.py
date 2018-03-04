import gensim.models as gm
import pandas as pd
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

## Cargamos los datos:
## ===================

# ruta mac:
filepath = 'Data/words_source_v2.2.csv'
# ruta windows:
# filepath = ''
data = pd.read_csv(filepath, sep = ';')
data.head()

data = data[['Pos1', 'R1', 'R2', 'R3', 'R4', 'R5']]

## Cargamos el modelo:
## ===================

# ruta mac:
route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
# route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

## Comenzamos con la representación:
## =================================

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

def apply_PCA(dictionary):
    ''' Devuelve el resultado de aplicar el PCA a un diccionario apropiado '''
    X = model[dictionary]
    pca = PCA(n_components = 2)
    result = pca.fit_transform(X)
    return result

def graphic_representation(name,result_POS, R1, R2, R3, R4, R5):
    '''
    Graficamos el resultado de aplicar el PCA
    INPUT:
    ------
        - name: string, nombre del archivo a guardar (ruta incluída)
        - result_POS:
        - R1, ..., R5:

    OUTPUT:
        - None
    -------
    '''

    plt.scatter(result_POS[:, 0][:2], POS[:, 1][:2], c = 'green', label = 'Word')
    plt.scatter(R1[:, 0][:2], R1[:, 1][:2], c = 'red', label = 'First resoult')
    plt.scatter(R2[:, 0][2:], R2[:, 1][2:], c = 'blue', label = 'other resoults')
    plt.scatter(R3[:, 0][2:], R3[:, 1][2:], c = 'blue')
    plt.scatter(R4[:, 0][2:], R4[:, 1][2:], c = 'blue')
    plt.scatter(R5[:, 0][2:], R5[:, 1][2:], c = 'blue')

    # función dentro de la principal para ahorrarme trabajo:
    def lettering(dictionary):
        words = list(dictionary)
        for i, word in enumerate(words):
        	print(i, word)
        	plt.annotate(word, xy = (result[i, 0], result[i, 1]))

    lettering(result_POS)
    lettering(R1)
    lettering(R2)
    lettering(R3)
    lettering(R4)
    lettering(R5)

    plt.legend()
    plt.savefig(name)
    plt.show()
