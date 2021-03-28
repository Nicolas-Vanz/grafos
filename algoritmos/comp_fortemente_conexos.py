from grafo import Grafo

def componentes_conexas_resultado(ancestrais):
    componentes = []
    for i in range(len(ancestrais)):
        if (ancestrais[i] == None):
            c = [i]
            proximos = [i]
            while(len(proximos) > 0):
                atual = proximos.pop()
                for index, value in enumerate(ancestrais):
                    if (value == atual):
                        proximos.append(index)
                        c.append(index)
            c.sort()
            componentes.append(c)
    
    for componente in componentes:
        print(",".join(list(map(lambda x: str(x + 1), componente))))

def componentes_conexas(grafo):
    vertices = [int(i) for i in range(grafo.vertices)]
    visitados, ancestrais, tempos = dfs(grafo, vertices)
    grafo.transpor()
    vertices.sort(reverse = True, key=lambda x: tempos[x])
    visitados, ancestrais, tempos = dfs(grafo, vertices)
    return ancestrais

def dfs(grafo, ordem_vertices):
    visitados = [False] * (grafo.vertices)
    ancestrais = [None] * (grafo.vertices)
    tempos = [grafo.inf] * (grafo.vertices)
    tempo = 0
    for vertice in ordem_vertices:
        if (not visitados[vertice]):
            visitados, ancestrais, tempos, tempo = dfs_visit(
                grafo, vertice, visitados, ancestrais, tempos, tempo)

    return visitados, ancestrais, tempos

def dfs_visit(grafo, vertice, visitados, ancestrais, tempos, tempo):
    visitados[vertice] = True
    tempo += 1
    for vizinho in grafo.vizinhos(vertice):
        if (not visitados[vizinho]):
            ancestrais[vizinho] = vertice
            visitados, ancestrais, tempos, tempo = dfs_visit(
                grafo, vizinho, visitados, ancestrais, tempos, tempo)
    tempo += 1
    tempos[vertice] = tempo + 1
    return visitados, ancestrais, tempos, tempo

if __name__ == "__main__":
    grafo = Grafo("../entradas/ent.txt")
    componentes_conexas_resultado(componentes_conexas(grafo))
