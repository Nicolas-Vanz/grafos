from grafo import Grafo


def hierholzer_resultado(tupla):
	validez = tupla[0]
	ciclo = tupla[1]
	if not validez:
		return ("0")
	return ("1\n" + ",".join(map(lambda x: str(x + 1), ciclo)))

def hierholzer(grafo):
	vertices_disponiveis = {i : grafo.vizinhos(i) for i in range(grafo.vertices)}

	for value in vertices_disponiveis.values():
		if len(value) % 2 != 0:
			return (False, [])

	inicio = -1
	for key, value in vertices_disponiveis.items():
		if len(value) > 0:
			inicio = key
			break
	if inicio == -1:
		return (False, [])

	ciclo = [inicio]

	while True:
		for vertice in ciclo:
			if len(vertices_disponiveis[vertice]) > 0:
				inicio = vertice
				atual = vertice
				break

		subciclo = [atual]

		while True:
			proximo = vertices_disponiveis[atual].pop()
			vertices_disponiveis[proximo].remove(atual)
			subciclo.append(proximo)
			atual = proximo
			if atual == inicio:
				break

		indice = ciclo.index(inicio)
		ciclo[indice:indice + 1] = subciclo

		continuar = False
		for key, value in vertices_disponiveis.items():
			if len(value) > 0:
				continuar = True
				break

		if not continuar: break

	return (True, ciclo)

if __name__ == "__main__":
	grafo = Grafo("../entradas/ent.txt")
	print(hierholzer_resultado(hierholzer(grafo)))
