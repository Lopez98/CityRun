from random import randint

class LogicaObstaculo(object):

	""" Clase que se encarga de controlar la creacion de los obstaculos que el jugador debe impedir"""

	def __init__(self):
		self.posX = 640
		self.posY = 296
		self.velocidad = 120

	def crearObstaculo(self, lista):
		if self.velocidad == 240:
			random = randint(1,2)
			if random == 1:
				lista.append((self.posX ,self.posY))

		elif self.velocidad == 0:
			self.velocidad = 241

		self.velocidad -= 1

		return lista

	def moverObstaculo(self, lista):
		lenght = len(lista)
		for i in range(lenght):
			lista[i] = (lista[i][0]-1, lista[i][1])

		return lista

	def borrarObstaculo(self, lista):
		lenght = len(lista)
		if (-20,296) in lista:
			lista.remove((-20,296))

		return lista
