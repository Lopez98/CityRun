class Rectangulo(object):

	"""Figura rectangular"""

	def __init__(self, punto, ancho, alto):
		self.rectangulo = (punto[0], punto[1], ancho, alto)

	def getRect(self):
		return self.rectangulo
