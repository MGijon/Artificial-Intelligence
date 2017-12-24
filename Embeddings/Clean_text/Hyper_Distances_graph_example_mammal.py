from nltk.corpus import wordnet as wn
import networkx as nx
import matplotlib.pyplot as plt

mammal = wn.synsets('mammal')[0]

# set of tuples (synset, distance)
Mammals = mammal.hypernym_distances()

G = nx.Graph()

Nodes = [j[0].name() for j in Mammals]
Origin = [s[0].name() for s in Mammals if s[1] == 0]

Edges = [(Origin[0], s[0].name(), s[1]) for s in Mammals]

G.add_nodes_from(Nodes)
G.add_weighted_edges_from(Edges)

nx.draw(G, with_labels = True, node_color = 'yellow')
plt.savefig('Hyper_Distances_graph_example_mammal.png')
plt.show()
