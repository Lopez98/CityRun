
class LogicaCamino(object):

	""" Clase que se encarga de darle la animacion al camino por el que el jugardor se desplaza """

	def __init__(self, velocidad):
		self.posX1 = 0
		self.posX2 = 640
		self.velocidad = velocidad
		self.v = velocidad
		

	def getPos(self):

		if self.posX1 == -640:
			self.posX1 = 640
		if self.posX2 == -640:
			self.posX2 = 640

		if self.velocidad == 0:
			self.posX1 -= 1
			self.posX2 -= 1

			self.velocidad = self.v

		elif self.velocidad != 0:
			self.velocidad -= 1

		return self.posX1,self.posX2