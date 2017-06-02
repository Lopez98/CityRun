class Rectangulo(object):

	"""Figura rectangular"""

	def __init__(self):
		pass

	def getRect(self, punto, ancho, alto):
		rectangulo = (punto[0], punto[1], ancho, alto)
		return rectangulo
