from random import randint

class LogicaBillete(object):

	""" Clase que se encarga de controlar la creacion de los billetes que el jugador recolecta"""

	def __init__(self):
		self.posX = 640
		self.posY = 140
		self.velocidad = 0
		self.sprite = 0
		self.v = 24

	def crearBillete(self, lista):
		if self.velocidad == 960:
			random = randint(1,3)
			if random == 1:
				lista.append((self.posX ,self.posY))

		elif self.velocidad == 0:
			self.velocidad = 961

		self.velocidad -= 1

		return lista

	def moverBillete(self, lista):
		lenght = len(lista)
		for i in range(lenght):
			lista[i] = (lista[i][0]-1, lista[i][1])

		return lista

	def borrarBillete(self, lista):
		lenght = len(lista)
		if (-20,140) in lista:
			lista.remove((-20,140))

		return lista

	def getSprite(self):
		if self.v == 0:
			if self.sprite != 7:
				self.sprite += 1

			else:
				self.sprite = 0

			self.v = 24

		else:
			self.v -= 1

		return self.sprite
