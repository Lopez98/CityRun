import pygame
from estados.EstadoInicial import EstadoInicial
from estados.EstadoJugar import EstadoJugar
from estados.EstadoPerder import EstadoPerder

class CityRun(object):
	
	""" Clase principal que va a controlar los estados del juego """

	def __init__(self):

		pygame.init()

		ventana = pygame.display.set_mode((640,384))
		pygame.display.set_caption("City Run Game")


		estado = 1
		salto = False
		clock = pygame.time.Clock()
		click = False

		while True:

			ventana.fill((200,50,100))

			clock.tick(240)

			mouse = pygame.mouse.get_pos()

			if estado == 1:
				EstadoInicial(click)

			elif estado == 2:
				if salto == False:
					if EstadoJugar().correr():
						estado = 3
					
				elif salto == True:
					salto = EstadoJugar().saltar()[0]

			elif estado == 3:
				EstadoPerder()


			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					pygame.quit()

				if estado == 1:
					if mouse[0]>192 and mouse[0]<448 and mouse[1]>128 and mouse[1]<256:
						click = True
						if evento.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()==(1,0,0):
							estado = 2
					else:
						click = False

				elif estado == 2:
					if evento.type == pygame.KEYDOWN:
						if evento.key == pygame.K_UP:
							salto = True

				elif estado == 3:
					if evento.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()==(1,0,0):
						estado = 2

			pygame.display.update()
