import math
import os

# IMPORTANTE:
# os vertices sao descritos nos arquivos a partir de 1 mas são
# armazenados a partir do zero. Quando imprimir algum vértice, somar 1 ao valor
# dele

class Grafo:
	def __init__(self, arquivo):
		# representa um numero infinito
		self.inf = math.inf
		self.matriz = None
		self.vertices = None
		self.fonte = None
		self.destino = None
		self.rotulo = None
		self.tipo = None

		self.__construir(arquivo)
	
	def __setup_txt(self, lines):
		self.vertices = int(lines[0].split()[1])
		# preenche o grafo com arestas de peso infinito
		self.matriz = [[self.inf for i in range(self.vertices)] for j in range(self.vertices)]
		# salva os rotulos
		self.rotulos = {
		int(rotulo[0])-1 : rotulo[1] for rotulo in [i.split(' ', 1) for i in lines[1:self.vertices + 1]]
		}

		tipo = lines[self.vertices + 1] 
		if (tipo == "*edges"):
			self.tipo = "e"
		elif (tipo == "*arcs"):
			self.tipo = "a"
		else:
			print("tipo de grafo nao identificado. No arquivo é especificado *edges ou *arcs?")
			exit()

	def __setup_gr(self, lines):
		for line in lines:
			i = line[0]
			if i == "p":
				line = line.split()
				self.vertices = int(line[2])
			elif i == "n":
				line = line.split()
				v = line[2]
				if v == "t":
					self.destino = int(line[1]) - 1
				elif v == "s":
					self.fonte = int(line[1]) - 1
			elif i == "a":
				self.tipo = "a"
				break
			elif i == "e":
				self.tipo = "e"
				break
		if (not self.vertices):
			print("numero de vertices nao reconhecido")
			exit()
		if (not self.tipo):
			print("tipo de grafo nao identificado. No arquivo é especificado \'e\' ou \'a\'?")
			exit()
		self.matriz = [[self.inf for i in range(self.vertices)] for j in range(self.vertices)]

	def __construir(self, arquivo):
		lines, arquivo_extensao = self.__ler_arquivo(arquivo)
		lines = list(filter(lambda x: x != "", lines))
		if arquivo_extensao == ".gr":
			self.__construir_gr(lines)
		else:
			self.__construir_txt(lines)

	def __construir_gr(self, lines):
		self.__setup_gr(lines)
		if (self.tipo == "e"):
			lines = list(filter(lambda x: x[0] == "e", lines))
			self.__construir_nao_dirigido_gr(lines)
		elif (self.tipo == "a"):
			lines = list(filter(lambda x: x[0] == "a", lines))
			self.__construir_dirigido_gr(lines)
		else:
			self.__erro()

	def __construir_txt(self, lines):
		self.__setup_txt(lines)
		if (self.tipo == "e"):
			self.__construir_nao_dirigido(lines[self.vertices + 2:])
		elif (self.tipo == "a"):
			self.__construir_dirigido(lines[self.vertices + 2:])
		else:
			self.__erro()
			

	def __ler_arquivo(self, arquivo):
		arquivo_nome, arquivo_extensao = os.path.splitext(arquivo)

		try:
			with open(arquivo, "r") as f:
				lines = [i for i in f.read().splitlines()]
		except FileNotFoundError:
			print("arquivo nao encontrado: %s" % arquivo)
			exit()

		return lines, arquivo_extensao

	def __construir_nao_dirigido_gr(self, arestas):
		ponderado = True if len(arestas[0].split()) > 3 else False
		peso = 1
		for aresta in arestas:
			aresta = aresta.split()
			v1 = int(aresta[1]) - 1
			v2 = int(aresta[2]) - 1
			if (ponderado):
				peso = float(aresta[3])
			self.matriz[v1][v2] = peso
			self.matriz[v2][v1] = peso
	
	def __construir_dirigido_gr(self, arcos):
		for arco in arcos:
			arco = arco.split()
			origem = int(arco[1]) - 1
			destino = int(arco[2]) - 1
			peso = float(arco[3])
			self.matriz[origem][destino] = peso

	def __construir_nao_dirigido(self, arestas):
		for aresta in arestas:
			aresta = aresta.split()
			aresta[0] = int(aresta[0])
			aresta[1] = int(aresta[1])
			aresta[2] = float(aresta[2])
			self.matriz[aresta[0] - 1][aresta[1] - 1] = aresta[2]
			self.matriz[aresta[1] - 1][aresta[0] - 1] = aresta[2]
	
	def __construir_dirigido(self, arcos):
		for arco in arcos:
			arco = arco.split()
			arco[0] = int(arco[0])
			arco[1] = int(arco[1])
			arco[2] = float(arco[2])
			self.matriz[arco[0] - 1][arco[1] - 1] = arco[2]

	def __erro(self):
		print("erro")
		exit()

	def qtdVertices(self):
		return self.vertices

	def qtdArestas(self):
		counter = 0
		for i in range(self.vertices):
			for j in range(0, i + 1):
				if self.matriz[i][j] != self.inf:
					counter += 1
		return counter

	def arestas(self):
		return [(i, j, self.matriz[i][j]) for i in range(self.vertices) for j in range(self.vertices) if self.matriz[i][j] != self.inf]

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
