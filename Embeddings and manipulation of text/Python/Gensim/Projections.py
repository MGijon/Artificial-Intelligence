import gensim.models as gm
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

## (1): Cargamos el modelo que utilizaremos:
## ===

# ruta mac:
# route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
# ruta windows:
route = 'D:\GIT\Data\GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

## (2): Creamos un diccionario con las palabras que nos interesan:
## ===

words_list = ['man', 'women', 'king', 'queen']

dict = {}
for i in words_list:
	dict[i] = model.wv.vocab[i]

## (3): Aplicamos un modelo PCA 2-dimensional a los vectores:
## ===

X = model[dict]
pca = PCA(n_components = 2)
result = pca.fit_transform(X)

## (4): Imprimimos los resultados:
## ===

def funcion1():
	########################################################
	# Esta función imprime un scatter plot con la palabras
	# en la words_list sin colores diferenciados ni flechas.
	# ------------------------------------------------------
	# INPUT: ninguno
	# ------
	#
	# OUTPUT: ninguno
	# -------
	########################################################

	plt.scatter(result[:, 0], result[:, 1])
	words = list(dict)
	for i, word in enumerate(words):
		print(i, word)
		plt.annotate(word, xy = (result[i, 0], result[i, 1]))

	plt.savefig('Man-King.png')
	plt.title('Words')
	plt.show()

funcion1()

def funcion2():
	########################################################
	# Esta función imprime un scatter plot con la palabras
	# en la words_list con colores diferenciados y no flechas.
	# --------------------------------------------------------
	# INPUT: ninguno
	# ------
	#
	# OUTPUT: ninguno
	# -------
	########################################################

	plt.scatter(result[:, 0][:2], result[:, 1][:2], c = 'green', label = 'input')
	plt.scatter(result[:, 0][2:], result[:, 1][2:], c = 'red', label = 'output')
	words = list(dict)
	for i, word in enumerate(words):
		print(i, word)
		plt.annotate(word, xy = (result[i, 0], result[i, 1]))

	plt.legend(loc = 2)
	plt.savefig('Man-King_V2.png')
	plt.title('Words')
	plt.show()

funcion2()


def funcion3():
	########################################################
	# Esta función imprime un scatter plot con la palabras
	# en la words_list con colores diferenciados y flechas.
	# ------------------------------------------------------
	# INPUT: ninguno
	# ------
	#
	# OUTPUT: ninguno
	# -------
	########################################################

	plt.scatter(result[:, 0][:2], result[:, 1][:2], c = 'green', label = 'input')
	plt.scatter(result[:, 0][2:], result[:, 1][2:], c = 'red', label = 'output')
	words = list(dict)
	for i, word in enumerate(words):
		print(i, word)
		plt.annotate(word, xy = (result[i, 0], result[i, 1]))

	plt.legend(loc = 2)
	# flechas man -> king, women -> queen
	plt.annotate('texto', xy = result[1],
				  arrowprops = {'arrowstyle' : '->', 'connectionstyle' : 'arc3'} )
	plt.savefig('Man-King_V3.png')
	plt.title('Words')
	plt.show()

funcion3()

########################
result
result[0] # posición de 'man'
result[1] # posición de
result[2] # posición de
result[3] # posición de

result[:, 0][:2]
result[:, 1][:2]

result[:, 0][2:]
result[:, 1][2:]

print(model.most_similar( positive = ['Japan', 'France'], negative = ['Tokio'], topn = 1))

print(model.most_similar( positive = ['Japan', 'France'], negative = ['Paris'], topn = 1))

print(model.most_similar( positive = ['surgeon', 'women'], negative = ['man'], topn = 1))

print(model.most_similar( positive = ['surgeon', 'mother'], negative = ['father'], topn = 1))

print(model.most_similar( positive = ['doctor', 'mother'], negative = ['father'], topn = 1))

print(model.most_similar( positive = ['doctor', 'she'], negative = ['he'], topn = 1))

print(model.most_similar( positive = ['surgeon', 'she'], negative = ['he'], topn = 1))

print(model.most_similar( positive = ['coward', 'she'], negative = ['he'], topn = 1))
