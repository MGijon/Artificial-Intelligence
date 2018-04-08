from nltk.corpus import wordnet as wn

conjunto = []
syn = wn.synsets('dog')[0]

lista = syn.hyponyms()

def adding_elements(syn):
    '''
    Añadimos ramas al conjunto para cada nodo
    '''
    syn = syn.hyponyms()
    if syn != []:
        for i in syn:
            conjunto.append(i)

def numero_ramas(syn):
    '''
    Calculamos el número de hijos de cada nodo del árbol
    '''
    return len(syn.hyponyms())
