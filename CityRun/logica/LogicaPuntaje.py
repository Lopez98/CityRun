class LogicaPuntaje(object):

	"""Controla en puntaje que marca el jugador"""

	def __init__(self):
		archivo = open('logica/puntaje.txt','r')
		self.maxPuntaje = archivo.readline()
		archivo.close()
		self.puntaje = 0
		self.vel = 256

	def getPuntaje(self, juego):
		if juego == False:
			if self.vel == 0:
				self.puntaje += 1
				self.vel = 256

			else:
				self.vel -= 1
		else:
			if self.puntaje > int(self.maxPuntaje):
				self.maxPuntaje = str(self.puntaje)

				archivo = open('logica/puntaje.txt','w')
				archivo.write(self.maxPuntaje)
		return self.puntaje, self.maxPuntaje
