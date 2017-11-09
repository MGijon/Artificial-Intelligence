from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

# defining training data
sentences = [['Hi', 'doggy'],
             ['Oh', 'actually', 'Johnny', 'I', 'got', 'a', 'I', 'got', 'a', 'little', 'bit', 'of', 'a', 'tragedy'],
             ['You', 'are', 'tearing', 'me', 'apart', 'Lisa'],
             ['Thank', 'you', 'honey', 'this', 'is', 'a', 'beautiful', 'party'],
             ['You', 'invited', 'all', 'my', 'friends', 'good', 'thinking'],
             ['All', 'men', 'are', 'assholes'],
             ['Men', 'and', 'women', 'use', 'and', 'abuse', 'each', 'other', 'all', 'the', 'time', 'there', 'is',
              'nothing', 'wrong', 'with', 'it'],
             ['Marriage', 'has', 'nothing', 'to', 'do', 'with', 'love']]

# training model
model = Word2Vec(sentences, min_count = 1)

# fit a 2d PCA model to the vectors
X = model[model.wv.vocab]
pca = PCA(n_components = 2)
result = pca.fit_transform(X)
print(len(result))   # 53

# create a scatter plot of the projection
plt.scatter(result[:, 0], result[:, 1])
words = list(model.wv.vocab)
for i, word in enumerate(words):
	plt.annotate(word, xy = (result[i, 0], result[i, 1]))

plt.title('Some sentences of "The Room" (2003)')
plt.show()


# source : https://machinelearningmastery.com/develop-word-embeddings-python-gensim/
# source sentences : The Room (2003)