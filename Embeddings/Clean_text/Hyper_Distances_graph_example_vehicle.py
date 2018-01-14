from nltk.corpus import wordnet as wn
import networkx as nx
import matplotlib.pyplot as plt

Vehicle = wn.synsets('vehicle')[0]

# set of tuples (synset, distances)
first_branch = Vehicle.hypernym_distances()
#second_brach = [i[0].hypernym_distances() for i in first_branch]
# tuple (origin, lista((synset, distances)))
second_brach = [(i[0], list(i[0].hypernym_distances())) for i in first_branch]

type(second_brach)
type(second_brach[0])
type(second_brach[0][0])
type(second_brach[0][1])
type(second_brach[0][1][2])

# create an object Graph
G = nx.Graph()

# Define Nodes and Origin(s) (first and second generations)
first_Nodes = [j[0].name() for j in first_branch]
first_Origin = [j[0].name() for j in first_branch if j[1] == 0]

second_Nodes = []
for n in second_brach: # n is a tuple (synset, list of tuples)
    for m in n:
        for h in m[1]:
            second_Nodes.append(m[1].name())
'''
second_Origins = []
for n in second_brach:
    for m in n:
        if m[1] == 0:
            second_Origins.append(m[0].name())
'''
# Define the edges
first_Edges = [(first_Origin[0], s[0].name(), s[1]) for s in first_branch]

# ARREGLAR ESTE DESAGISADO MAÑANA
second_Edges = []
for n in second_brach:
    for m in n[1]:
        if list(m)[1] == 0:
            second_Edges.append([m[0], s[0].name(), s[1]] for s in n[1])


G.add_nodes_from(first_Nodes)
G.add_nodes_from(second_Nodes)
G.add_weighted_edges_from(first_Edges)
# FALTA AÑADIR LA SEGUNDA GENERACIÓN DE EJES

nx.draw(G, with_labels = True, node_color = 'yellow')
plt.show()
