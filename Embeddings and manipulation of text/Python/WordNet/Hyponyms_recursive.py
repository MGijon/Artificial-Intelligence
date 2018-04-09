from nltk.corpus import wordnet as wn

SYN = wn.synsets('dog')[0]

lista = SYN.hyponyms()

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

def lista_hijos(syn):
    '''
    Devuelve una lista con el número de hijos de cada nodo de sus hijos
    '''
    return [numero_ramas(i) for i in syn.hyponyms()]

def Cest_fini(lista):
    '''
    Si no hay hijos nos devuelve un True
    '''
    if len(lista) == 0:
        return True
    else:
        lista = []
        return False

def recursiva(syn):
    '''
    Función recursiva que devuelve una lista con los hypónimos al completo
    '''
    conjunto = []
    if numero_ramas(syn) == 0:
        conjunto.append(syn)
    else:
        conjunto.append(syn)
        for i in syn.hyponyms():
            recursiva(i)
    return conjunto

recursiva(SYN)
