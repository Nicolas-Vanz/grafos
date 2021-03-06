from grafo import Grafo


def floydwarshall_resultado(grafo):
    for i in range(grafo.vertices):
        print("%d: " % (i + 1) + ",".join(map(str, grafo[i])))
    print("\ninf: representa uma aresta de peso infinito (não existe)")

def floydwarshall(grafo):
    for k in range(grafo.vertices):
        for i in range(grafo.vertices):
            for j in range(grafo.vertices):
                grafo[i][j] = min(grafo[i][j], grafo[i][k] + grafo[k][j])
    return grafo

if __name__ == "__main__":
    grafo = Grafo("../entradas/ent.txt")
    floydwarshall_resultado(floydwarshall(grafo))