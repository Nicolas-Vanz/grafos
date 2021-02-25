from grafo import Grafo

def busca_largura(grafo, vertice):
	vertice -= 1
	grafo.validar_vertice(vertice)
	visitados = [False] * (grafo.vertices)
	proximo = [vertice]
	nivel = 0
	while True:
		atual = proximo.copy()
		proximo = []
		for i in range(len(atual)):
			v = atual[i]
			visitados[v] = True
			vizinhos_nao_visitados = list(filter(lambda x : not visitados[x], grafo.vizinhos(v)))
			for x in vizinhos_nao_visitados: visitados[x] = True
			proximo.extend(vizinhos_nao_visitados)
		print("%d:" % (nivel), end = ' ')
		print(",".join(map(lambda x: str(x + 1), atual)))
		if len(proximo) == 0:
			break
		nivel += 1

if __name__ == "__main__":
	grafo = Grafo("../entradas/ent.txt")
	v = int(input("vertice inicial:\n"))
	busca_largura(grafo, v)
