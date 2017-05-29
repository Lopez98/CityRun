
class LogicaJugador(object):

	"""Esta clase se encarga de controlar la animacion del personaje cuando realiza una de las acciones posibles"""

	def __init__(self, velocidad):
		self.sprite = 0
		self.velocidad = velocidad
		self.v = velocidad
		self.posY = 200
		self.accion = True
		self.salto = True

	def getSprite(self):

		if self.sprite == 7:
			self.sprite = 0

		if self.velocidad == 0:
			self.sprite += 1

			self.velocidad = self.v

		elif self.velocidad != 0:
			self.velocidad -= 1

		return self.sprite	
	
	def getSalto(self):
		self.salto = True
		if self.accion:
			if self.posY > 100:
				self.posY -= 2

			else:
				self.accion = False

		else:
			if self.posY < 200:
				self.posY += 1

			else:
				self.accion = True
				self.salto = False

		return self.posY,self.salto