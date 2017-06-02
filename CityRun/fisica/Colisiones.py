import pygame

class Colisiones(object):

	"""Determina colisiones entre figuras"""

	def __init__(self):
		pass

	def getColision(self, rect1, rect2):
		rectangulo1 = pygame.Rect(rect1)
		rectangulo2 = pygame.Rect(rect2)

		return rectangulo1.colliderect(rectangulo2)		
