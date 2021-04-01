from grafo import Grafo
from functools import reduce


def set_union(sets, u, v):
    if (sets[u] < sets[v]):
        sets[u] += sets[v]
        sets[v] = u
    else:
        sets[v] += sets[u]
        sets[u] = v
    return sets
 
def set_find(sets, u):
    x = u
 
    while (sets[x] >= 0):
        x = sets[x]
 
    while (u != x):
        v = sets[u]
        sets[u] = x
        u = v
    
    return sets, x

def kruskal_resultado(resultado):
    print(sum([i[2] for i in resultado]))
    print(", ".join(map(lambda x: "%d-%d" % (x[0] + 1,x[1] + 1), resultado)))

def kruskal(grafo):
    sets = [-1] * (grafo.vertices)
    arestas = grafo.arestas()
    arestas.sort(key = lambda x: x[2])
    resultado = []

    for aresta in arestas:
        u = aresta[0]
        v = aresta[1]
        sets, su = set_find(sets, u)
        sets, sv = set_find(sets, v)
        if (su != sv):
            resultado.append(aresta)
            sets = set_union(sets, su, sv)
    return resultado


if __name__ == "__main__":
    grafo = Grafo("../entradas/ent.txt")
    kruskal_resultado(kruskal(grafo))
    