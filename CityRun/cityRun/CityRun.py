import pygame
from estados.EstadoInicial import EstadoInicial
from estados.EstadoJugar import EstadoJugar

class CityRun(object):
	
	""" Clase principal que va a controlar los estados del juego """

	def __init__(self):

		pygame.init()

		ventana = pygame.display.set_mode((640,384))
		pygame.display.set_caption("City Run Game")


		estado = 1
		salto = False
		clock = pygame.time.Clock()

		while True:

			ventana.fill((200,50,100))

			clock.tick(240)

			if estado == 1:
				EstadoInicial()

			elif estado == 2:
				if salto == False:
					EstadoJugar().correr()
				elif salto == True:
					salto = EstadoJugar().saltar()

			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					pygame.quit()

				if estado == 1:
					if evento.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()==(1,0,0):
						estado = 2

				elif estado == 2:
					if evento.type == pygame.KEYDOWN:
						if evento.key == pygame.K_UP:
							salto = True

			pygame.display.update()
