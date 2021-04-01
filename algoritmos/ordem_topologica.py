from grafo import Grafo

def dfs_ordenacao_topologica_resultado(resultado):
    print(" -> ".join(map(lambda x: grafo.rotulo(x), resultado)))

def dfs_ordenacao_topologica(grafo):
    visitados = [False] * (grafo.vertices)
    o = []
    for i in range(grafo.vertices):
        if (not visitados[i]):
            visitados, o = dfs_visit(grafo, visitados, o, i)
    
    return (o)

def dfs_visit(grafo, visitados, o, v):
    visitados[v] = True
    for i in grafo.vizinhos(v):
        if (not visitados[i]):
            visitados, o = dfs_visit(grafo, visitados, o, i)
    o.insert(0, v)

    return visitados, o


if __name__ == "__main__":
    grafo = Grafo("../entradas/ent.txt")
    dfs_ordenacao_topologica_resultado(dfs_ordenacao_topologica(grafo))
    