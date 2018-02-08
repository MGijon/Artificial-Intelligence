import pandas as pd
import gensim.models as gm

filepath = 'Data/words_source.csv'
data = pd.read_csv(filepath, sep = ';')

route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)
