from nltk.corpus import wordnet as wn
import networkx as nx
import matplotlib.pyplot as plt

Vehicle = wn.synsets('vehicle')[0]

# set of tuples (synset, distances)
first_branch = Vehicle.hypernym_distances()
#second_brach = [i[0].hypernym_distances() for i in first_branch]
# tuple (origin, lista((synset, distances)))
second_brach = [(i[0], list(i[0].hypernym_distances())) for i in first_branch]

# ----------------------------
type(second_brach)
type(second_brach[0])
type(second_brach[0][0])
type(second_brach[0][1])
type(second_brach[0][1][2])

for j in second_brach[0][1]:
    print(j)
    print(j[0])
second_brach[0][1][2]
second_brach[0][1][2][0]
second_brach[0][1][2][0].name()
for i in second_brach[0][1][2][0].lemmas():
    print(i)
# ----------------------------

# create an object Graph
G = nx.Graph()

# Define Nodes and Origin(s) (first and second generations)
first_Nodes = [j[0].name() for j in first_branch]
first_Origin = [j[0].name() for j in first_branch if j[1] == 0]

second_Nodes = []
for n in second_brach[0][1]: # n is a tuple (synset, list of tuples)
    second_Nodes.append(n)
'''
second_Origins = []
for n in second_brach:
    for m in n:
        if m[1] == 0:
            second_Origins.append(m[0].name())
'''
# Define the edges
first_Edges = [(first_Origin[0], s[0].name(), s[1]) for s in first_branch]

# ARREGLAR ESTE DESAGISADO
second_Edges = []     # la construiré como una lista de listas
for n in second_brach:
    #print(n[0])
    #print(n[1])
    second_Edges.append((n[0],n[1]))
    #second_Edges.append([n[0][0], s[1].name(), s[1]] for s in n[0][0][1])

# ----------------------------
second_Edges
first_Edges

# ----------------------------

G.add_nodes_from(first_Nodes)
G.add_nodes_from(second_Nodes)
G.add_weighted_edges_from(first_Edges)
# FALTA AÑADIR LA SEGUNDA GENERACIÓN DE EJES
for j in second_Edges:
    G.add_weighted_edges_from(j)

znx.draw(G, with_labels = True, node_color = 'yellow')
plt.show()
