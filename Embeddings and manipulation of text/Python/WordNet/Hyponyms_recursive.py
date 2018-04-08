from nltk.corpus import wordnet as wn

conjunto = []
syn = wn.synsets('dog')[0]

lista = syn.hyponyms()

print(len(conjunto))

def adding_elements(syn):
    syn = syn.hyponyms()
    if syn != []:
        for i in syn:
            conjunto.append(i)

for i in lista:
    adding_elements(i)

print(len(conjunto))
