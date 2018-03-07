from nltk.corpus import wordnet as wn

# choose one of the synsets of 'Dog'
Dog = wn.synsets('dog')[0]
Dog

# set of tuples (synset, int)
Hyper_Distances_Dog = Dog.hypernym_distances()

# starting with the graph
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Nodes: the synset, when we painting it whe use the '.name()'
Nodes = [j[0] for j in Hyper_Distances_Dog]

# Weights: the distances to the sysnset 'Dog'
Weights = [j[1] for j in Hyper_Distances_Dog]

# Create a tuple (Synset origen, other one, weight)
    # Synset origen: take one suche us their distances is 0
Origen = [s[0] for s in Hyper_Distances_Dog if s[1] == 0]
#print(Origen)
Edges = [(Origen[0], j[0], j[1]) for j in Hyper_Distances_Dog]

type(Edges[0])
Edges[0]

# adding the nodes
G.add_nodes_from(Nodes)

# adding the weighted Edges
G.add_weighted_edges_from(Edges)

# let's try to paint it
nx.draw(G)
plt.savefig('Hyper_Distances_graph_example_dog_1.png')
plt.show()

nx.draw(G, with_labels = True)
plt.savefig('Hyper_Distances_graph_example_dog_2.png')
plt.show()

################################################################################
