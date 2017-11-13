from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt

# Training data set:
sentences = [['When', 'you', 'find', 'that', 'one', 'person', 'who', 'connects', 'you', 'to', 'the', 'world',
              'you', 'become', 'someone', 'different', 'someone', 'better'],
             ['When', 'that', 'person', 'is', 'taken', 'from', 'you', 'what', 'do', 'you', 'become', 'then']]

# Trainig Model:
model = Word2Vec(sentences, min_count = 1)

# Fit a 2d PCA model to the vectors:


X = model[model.wv.vocab]
print(type(X))                  # <class 'numpy.ndarray'>

'''PCA : Principal Componenet Analysis
   -----------------------------------
http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
'''
pca = PCA(n_components = 2)

result = pca.fit_transform(X)

print(len(result))              # 21, the same number than the number of words

'''
components_ : array, shape (n_components, n_features)
------------
Principal axes in feature space, representing the directions of maximum 
variance in the data. The components are sorted by explained_variance_.
'''

cont = pca.components_
print(type(cont))               # # <class 'numpy.ndarray'>
print(cont.shape)               # (2, 100)
#print(cont)

'''
explained_variance_ratio_ : array, shape (n_components,)
--------------------------
Percentage of variance explained by each of the selected components.
If n_components is not set then all components are stored and the sum 
of explained variances is equal to 1.0.
'''

cont = pca.explained_variance_ratio_
print(type(cont))               # <class 'numpy.ndarray'>
print(cont.shape)               # (2,)
print(cont)                     # [ 0.09041016  0.08380682]




# Scatter plot of the projection:

plt.scatter(result[:, 0], result[:, 1])
words = list(model.wv.vocab)
for i, word in enumerate(words):
	plt.annotate(word, xy = (result[i, 0], result[i, 1]))

plt.title('Some sentences of "Person of Interest 1x01, Pilot" (2003)')
plt.show()


