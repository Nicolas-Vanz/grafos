from grafo import Grafo

def dijkstra_resultado(tupla):
	distancias = tupla[0]
	caminhos = tupla[1]
	for destino, antecessor in caminhos.items():
		caminho = []
		while antecessor is not None:
			caminho.insert(0, antecessor)
			antecessor = caminhos[antecessor]
		caminho.append(destino)
		print(
			"%d: " % (destino + 1) + 
			",".join(map(lambda x: str(x + 1), caminho)) + 
			"; d=%.2f" % (distancias[destino])
			)

def dijkstra(grafo, origem):
	origem -= 1  # ajuste do vertice
	grafo.validar_vertice(origem)  # valida o vertice

	distancias = {vertice : grafo.inf for vertice in range(grafo.vertices)}
	caminho = {vertice : None for vertice in range(grafo.vertices)}
	distancias[origem] = 0
	vertices = [int(v) for v in range(grafo.vertices)]
	
	while vertices:
		# vertice nao visitado cuja distancia é minima aresta tem o menor custo
		atual = min(vertices, key=lambda vertice: distancias[vertice])

		# a aresta de menor custo tem peso infinito
		if (distancias[atual] == grafo.inf):
			break
		
		for vertice in list(filter(lambda x: x in vertices, grafo.vizinhos(atual))):
			rota = distancias[atual] + grafo.peso(atual, vertice)

			# caminho passando por vertice é menor que o menor caminho existente até entao
			if (rota < distancias[vertice]):
				distancias[vertice] = rota
				caminho[vertice] = atual
		
		vertices.remove(atual)

	return (distancias, caminho)

if __name__ == "__main__":
	grafo = Grafo("../entradas/ent.txt")
	vertice = int(input("vertice origem:\n"))
	dijkstra_resultado(dijkstra(grafo, vertice))