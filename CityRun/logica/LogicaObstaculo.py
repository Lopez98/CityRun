from random import randint

class LogicaObstaculo(object):

	""" Clase que se encarga de controlar la creacion de los obstaculos que el jugador debe impedir"""

	def __init__(self):
		self.posX = 640
		self.posY = 296
		self.velocidad = 24

	def crearObstaculo(self, lista):
		random = randint(1,240)
		if random == 1:
			lista.append((self.posX ,self.posY))

		return lista

	def moverObstaculo(self, lista):
		lenght = len(lista)
		for i in range(lenght):
			lista[i] = (lista[i][0]-1, lista[i][1])

		return lista
