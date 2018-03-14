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

edges = [((node_1, node_2), dis_1_2), ((node_1, node_3), dis_1_3),
         ((node_1, node_4), dis_1_4), ((node_2, node_3), dis_2_3),
         ((node_2, node_4), dis_2_4), ((node_3, node_4), dis_3_4)]

edges_2 = [x[0] for x in edges]

edges_W = [(node_1, node_2, dis_1_2), (node_1, node_3, dis_1_3),
          (node_1, node_4, dis_1_4), (node_2, node_3, dis_2_3),
           (node_2, node_4, dis_2_4), (node_3, node_4, dis_3_4)]

## EXAMPLE 1:
## ==========

plt.close()
H = nx.Graph()
H.add_nodes_from(nodes)
print(H.nodes())
H.add_edges_from(edges_2)
print(H.nodes())
nx.draw(H, pos = nx.circular_layout(H), nodecolor = 'r', edge_color = 'b')
plt.savefig('GRE_1.png')
plt.show()

## EXAMPLE 2:
## ==========

plt.close()
G = nx.Graph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges_W)
nx.draw(G, nodecolor = 'white', edge_color = 'b', with_labels = True)
plt.savefig('GRE_2.png')
plt.show()


## EXAMPLE 3:
## ==========

plt.close()
I = nx.Graph()
I.add_weighted_edges_from(edges_W)
position = nx.circular_layout(I)
nx.draw_networkx_nodes(I, position, nodelist = nodes,
                       nodecolor = 'white', nodesize = 500,
                       alpha = 0.8)
edge_labels = nx.draw_networkx_edge_labels(I ,pos = position)
plt.savefig('GRE_3.png')
plt.show()

## EXAMPLE 4:
## ==========

plt.close()
J = nx.Graph()
J.add_weighted_edges_from(edges_W)
position = nx.circular_layout(J)
nx.draw_networkx_nodes(J, position, nodelist = nodes,
                       nodecolor = 'b', nodesize = 500,
                       alpha = 0.1)
edge_labels = nx.draw_networkx_edge_labels(J ,pos = position)
#plt.savefig('GRE_4.png')
plt.show()
