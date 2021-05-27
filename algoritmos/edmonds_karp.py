from grafo import Grafo



def ford_fulkerson():
	global grafo
	
	fluxo = 0

	fonte = grafo.fonte if (grafo.fonte) else 0
	destino = grafo.destino if (grafo.destino) else (grafo.vertices - 1)
	
	while(True):	
		caminho = edmonds_karp(fonte, destino)
		
		if (not caminho):
			break

		fluxo_caminho = grafo.inf

		for i in range(len(caminho) - 1):
			fluxo_caminho = min(grafo[caminho[i]][caminho[i + 1]], fluxo_caminho)

		for i in range(len(caminho) - 1):
			grafo[caminho[i]][caminho[i + 1]] -= fluxo_caminho
		
		fluxo += fluxo_caminho

	print(fluxo)
	


def edmonds_karp(fonte, destino):
	global grafo

	visitados = [False] * grafo.vertices
	visitados[fonte] = True
	a = [None] * grafo.vertices

	q = [fonte]
	while (q):
		u = q.pop()
		vizinhos = grafo.vizinhos(u)
		for vizinho in vizinhos:
			if not visitados[vizinho] and grafo[u][vizinho] > 0.0:
				visitados[vizinho] = True
				a[vizinho] = u

				if (vizinho == destino):
					p = [destino]
					w = destino
					while (w != fonte):
						w = a[w]
						p.append(w)
					
					p.reverse()
					return p
				
				q.insert(0, vizinho)
	
	return []



if __name__ == "__main__":
	global grafo

	grafo = Grafo("../entradas/fluxo_maximo/gb128.gr")
	ford_fulkerson()
