from gensim.models import Word2Vec
from sklearn.decomposition import PCA

'''
PRINCIPAL COMPONENT ANALYSIS (PCA):
----------------------------------
Linear dimensionality reduction using Singular Value Decomposition of the data to project it
to a lower dimensional space.
'''

# CREATE A MODEL TO APPLY THE PCA:
sentences = [['Hi', 'doggy']]
model = Word2Vec(sentences, min_count = 1)
X = model[model.wv.vocab]

# PCA:
pca = PCA(n_components = 2)
result = pca.fit_transform(X)







# source : http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html