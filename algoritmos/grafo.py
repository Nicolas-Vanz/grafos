import math

# IMPORTANTE:
# os vertices sao descritos nos arquivos a partir de 1 mas são
# armazenados a partir do zero. Quando imprimir algum vértice, somar 1 ao valor
# dele

class Grafo:
	def __init__(self, arquivo):
		# representa um numero infinito
		self.inf = math.inf
		self.__contruir(arquivo)
		
	def __contruir(self, arquivo):
		lines = self.__ler_arquivo(arquivo)
		if (lines[self.vertices + 1] == "*edges"):
			self.__construir_nao_dirigido(lines[self.vertices + 2:])
		elif (lines[self.vertices + 1] == "*arcs"):
			self.__construir_dirigido(lines[self.vertices + 2:])
		else:
			print("tipo de grafo nao identificado. No arquivo é especificado *edges ou *arcs?")
			exit()

	def __ler_arquivo(self, arquivo):
		try:
			with open(arquivo, "r") as f:
				lines = [i for i in f.read().splitlines()]
		except FileNotFoundError:
			print("arquivo nao encontrado: %s" % arquivo)
			exit()
		
		self.vertices = int(lines[0].split()[1])
		# preenche o grafo com arestas de peso infinito
		self.matriz = [[self.inf for i in range(self.vertices)] for j in range(self.vertices)]
		# salva os rotulos
		self.rotulos = {
		int(rotulo[0])-1 : rotulo[1] for rotulo in [i.split(' ', 1) for i in lines[1:self.vertices + 1]]
		}
		return lines

	def __construir_nao_dirigido(self, arestas):
		for aresta in arestas:
			aresta = aresta.split()
			aresta[0] = int(aresta[0])
			aresta[1] = int(aresta[1])
			aresta[2] = float(aresta[2])
			self.matriz[aresta[0] - 1][aresta[1] - 1] = aresta[2]
			self.matriz[aresta[1] - 1][aresta[0] - 1] = aresta[2]
	
	def __construir_dirigido(self, arcos):
		for aresta in arcos:
			aresta = aresta.split()
			aresta[0] = int(aresta[0])
			aresta[1] = int(aresta[1])
			aresta[2] = float(aresta[2])
			self.matriz[aresta[0] - 1][aresta[1] - 1] = aresta[2]

	def qtdVertices(self):
		return self.vertices

	def qtdArestas(self):
		counter = 0
		for i in range(self.vertices):
			for j in range(0, i + 1):
				if self.matriz[i][j] != self.inf:
					counter += 1
		return counter

	def rotulo(self, v):
		self.validar_vertice(v)
		rotulo = self.rotulos[v]
		return rotulo

	def grau(self, v):
		return self.vertices - self.matriz[v].count(self.inf)

	def vizinhos(self, v):
		return [int(i) for i in range(self.vertices) if self.matriz[v][i] != self.inf]

	def haAresta(self, v1, v2):
		return True if self.matriz[v1][v2] != self.inf else False

	def peso(self, v1, v2):
		return self.matriz[v1][v2]
	
	def validar_vertice(self, vertice):
		if (vertice >= 0 and vertice < self.vertices):
			return
		print("vertice invalido")
		exit()
	
	def transpor(self):
		for i in range(self.vertices):
			for j in range(i):
				temp = self.matriz[i][j]
				self.matriz[i][j] = self.matriz[j][i]
				self.matriz[j][i] = temp

	def __getitem__(self, item):
		return self.matriz[item]