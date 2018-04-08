from nltk.corpus import wordnet as wn

SYN = wn.synsets('dog')[0]

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

def bucle_idiota(syn):
    '''
    Función recursiva que devuelve una lista con los hypónimos al completo
    '''
    conjunto = []
    conjunto.append(syn)
    last_branches = [x for x in syn.hyponyms()]
    while last_branches != []:
        for i in last_branches:
            conjunto.append(i)
            last_branches.remove(i)
            last_branches.append(i.hyponyms())

    return conjunto

bucle_idiota(SYN)
'''
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
'''
