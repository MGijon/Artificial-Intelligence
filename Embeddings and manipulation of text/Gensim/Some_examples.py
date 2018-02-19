import gensim.models as gm

route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

print(model.most_similar( positive = ['Japan', 'France'], negative = ['Tokio'], topn = 1))

print(model.most_similar( positive = ['Japan', 'France'], negative = ['Paris'], topn = 1))

print(model.most_similar( positive = ['surgeon', 'women'], negative = ['man'], topn = 1))

print(model.most_similar( positive = ['surgeon', 'mother'], negative = ['father'], topn = 1))

print(model.most_similar( positive = ['doctor', 'mother'], negative = ['father'], topn = 1))

print(model.most_similar( positive = ['doctor', 'she'], negative = ['he'], topn = 1))

print(model.most_similar( positive = ['surgeon', 'she'], negative = ['he'], topn = 1))

print(model.most_similar( positive = ['coward', 'she'], negative = ['he'], topn = 1))
