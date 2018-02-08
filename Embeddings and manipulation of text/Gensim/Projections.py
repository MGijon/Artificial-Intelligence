import gensim.models as gm
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

# fit a 2d PCA model to the vectors
X = model[model.wv.vocab]
pca = PCA(n_components = 2)
result = pca.fit_transform(X)

# create a scatter plot of the projection
plt.scatter(result[:, 0], result[:, 1])
words = list(model.wv.vocab)
for i, word in enumerate(words):
	plt.annotate(word, xy = (result[i, 0], result[i, 1]))

plt.title('Words')
plt.show()

#print(model.most_similar('doggy'))
#print(model.most_similar(positive = ['doggy', 'men'], negative = ['assholes'])) # perro - gilipollas + hombre
