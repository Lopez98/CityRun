import pygame

class Colisiones(object):

	"""Determina colisiones entre figuras"""

	def __init__(self, rect1, rect2):
		self.rect1 = pygame.Rect(rect1)
		self.rect2 = pygame.Rect(rect2)

	def getColision(self):
		return self.rect1.colliderect(self.rect2)		
