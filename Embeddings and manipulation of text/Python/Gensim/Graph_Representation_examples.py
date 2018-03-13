import pandas as pd
import gensim.models as gm
import networkx as nx
import matplotlib.pyplot as plt

route = '/Users/manuelgijonagudo/Documents/Programación/GIT/Data/GoogleNews-vectors-negative300.bin.gz'
model = gm.KeyedVectors.load_word2vec_format(route, binary = True)

node_1 = 'man'
node_2 = 'woman'
node_3 = 'king'
result = model.most_similar( positive = [node_2, node_3], negative = [node_1], topn = 1)
node_4 = result[0][0]

nodes = [node_1, node_2, node_3, node_4]

dis_1_2 = model.similarity(node_1, node_2)
dis_1_3 = model.similarity(node_1, node_3)
dis_1_4 = model.similarity(node_1, node_4)
dis_2_3 = model.similarity(node_2, node_3)
dis_2_4 = model.similarity(node_2, node_4)
dis_3_4 = model.similarity(node_3, node_4)

edges = [dis_1_2, dis_1_3, dis_1_4, dis_2_3, dis_2_4, dis_3_4]
