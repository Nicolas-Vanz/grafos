from grafo import Grafo


def get_sets(grafo):
	s1 = [0]
	s2 = []
	t = [False] * grafo.vertices
	t[0] = True
	
	i = 0
	while(False in t):
		vz = grafo.vizinhos(i)
		if (i in s1):
			for v in vz:
				if (not t[v]):
					s2.append(v)
					t[v] = True
		elif (i in s2):
			for v in vz:
				if (not t[v]):
					s1.append(v)
					t[v] = True
		
		i = (i + 1) % grafo.vertices
	return s1, s2 

def BFS(grafo, x, mate, d):
	q = []
	for v in x:
		if (mate[v] == -1):
			d[v] = 0
			q.insert(0, v)
		else:
			d[v] = grafo.inf
	
	d[-1] = grafo.inf
	
	while (q):
		v = q.pop()
		if (d[v] < d[-1]):
			vizinhos = grafo.vizinhos(v)
			for vizinho in vizinhos:
				if (d[mate[vizinho]] == grafo.inf):
					d[mate[vizinho]] = d[v] + 1
					q.insert(0, mate[vizinho])
	
	return d[-1] != grafo.inf, d

def DFS(grafo, mate, xx, d):
	if xx != -1:
		vizinhos = grafo.vizinhos(xx)
		for y in vizinhos:
			if (d[mate[y]] == d[xx] + 1):
				validez, d, mate2 = DFS(grafo, mate, mate[y], d)
				if (validez):
					mate = mate2.copy()
					mate[y] = xx
					mate[xx] = y
					return True, d, mate
		d[xx] = grafo.inf
		return False, d, mate
	return True, d, mate

def hopcroft_karp_resultado(resultado):
	m, mate, x = resultado

	print("valor: %d\n" % m)
	print("arestas: ")
	for v in x:
		print("%d - %d;" % (v + 1, mate[v] + 1), end = " ")
	print()

def hopcroft_karp(grafo):
	d = [grafo.inf] * (grafo.vertices + 1)
	mate = [-1] * (grafo.vertices)
	
	x, y = get_sets(grafo)
	m = 0

	while(True):
		validez, d = BFS(grafo, x, mate, d)
		if (not validez):
			break
		
		for xx in x:
			if (mate[xx] == -1):
				validez, d, mate2 = DFS(grafo, mate, xx, d)
				if (validez):
					mate = mate2.copy()
					m += 1
	return m, mate, x

if __name__ == "__main__":
	grafo = Grafo("../entradas/emparelhamento_maximo/gr512_30.gr")
	hopcroft_karp_resultado(hopcroft_karp(grafo))