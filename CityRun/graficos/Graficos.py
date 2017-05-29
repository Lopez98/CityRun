import pygame
from logica.LogicaCamino import LogicaCamino
from logica.LogicaJugador import LogicaJugador
from logica.LogicaDificultad import LogicaDificultad
from logica.LogicaObstaculo import LogicaObstaculo

class Graficos(object):
	
	""" Esta clase controla toda la parte grafica del juego"""
	pygame.init()
	
	ventana = pygame.display.set_mode((640,384))

	""" Objetos """
	LogicaCamino = LogicaCamino(0)
	LogicaJugador = LogicaJugador(16)
	LogicaObstaculo = LogicaObstaculo()

	""" Imagenes que va a utilizar el juego"""
	LOGO = pygame.image.load("recursos/botones/logo.png")
	VACIO = pygame.image.load("recursos/botones/vacio.png")
	CONFIGURAR = pygame.image.load("recursos/botones/configurar.png")
	PAUSA = pygame.image.load("recursos/botones/pausa.png")

	JUGADOR_1 = pygame.image.load("recursos/personaje/1.png")
	JUGADOR_2 = pygame.image.load("recursos/personaje/2.png")
	JUGADOR_3 = pygame.image.load("recursos/personaje/3.png")
	JUGADOR_4 = pygame.image.load("recursos/personaje/4.png")
	JUGADOR_5 = pygame.image.load("recursos/personaje/5.png")
	JUGADOR_6 = pygame.image.load("recursos/personaje/6.png")
	JUGADOR_7 = pygame.image.load("recursos/personaje/7.png")
	JUGADOR_8 = pygame.image.load("recursos/personaje/8.png")

	FONDO = pygame.image.load("recursos/fondo/fondo.png")
	CAMINO = pygame.image.load("recursos/fondo/camino.png")

	BARRERA = pygame.image.load("recursos/obstaculos/barrera.png")
	CONO = pygame.image.load("recursos/obstaculos/cono.png")

	BILLETE_1 = pygame.image.load("recursos/billete/1.png")
	BILLETE_2 = pygame.image.load("recursos/billete/2.png")
	BILLETE_3 = pygame.image.load("recursos/billete/3.png")
	BILLETE_4 = pygame.image.load("recursos/billete/4.png")
	BILLETE_5 = pygame.image.load("recursos/billete/5.png")
	
	def __init__(self, estado):
		self.estado = estado
		self.sprites_Jugador = [Graficos.JUGADOR_1,Graficos.JUGADOR_2,Graficos.JUGADOR_3,Graficos.JUGADOR_4,Graficos.JUGADOR_5,Graficos.JUGADOR_6,Graficos.JUGADOR_7,Graficos.JUGADOR_8]
		self.sprites_Billete = [Graficos.BILLETE_1,Graficos.BILLETE_2,Graficos.BILLETE_3,Graficos.BILLETE_4,Graficos.BILLETE_5,Graficos.BILLETE_4,Graficos.BILLETE_3,Graficos.BILLETE_2]
		self.obstaculos = [(200,296)]
	
	def pintarLogo(self):
		Graficos.ventana.blit(Graficos.LOGO,(192,128))
		Graficos.ventana.blit(Graficos.CONFIGURAR,(600,8))


	def pintarFondo(self):
		Graficos.ventana.blit(Graficos.FONDO,(0,-100))

	def	pintarCamino(self):
		if self.estado == 1:
			posX = Graficos.LogicaCamino.getPos()
			Graficos.ventana.blit(Graficos.CAMINO,(posX[0],128))
			Graficos.ventana.blit(Graficos.CAMINO,(posX[1],128))

		elif self.estado == 2:
			posX = Graficos.LogicaCamino.getPos()
			Graficos.ventana.blit(Graficos.CAMINO,(posX[0],128))
			Graficos.ventana.blit(Graficos.CAMINO,(posX[1],128))

	def pintarPersonaje(self, saltar):
		if saltar == False:
			sprite = Graficos.LogicaJugador.getSprite()
			Graficos.ventana.blit(self.sprites_Jugador[sprite], (32,200))
		elif saltar == True:
			salto = Graficos.LogicaJugador.getSalto()
			Graficos.ventana.blit(self.sprites_Jugador[5], (32,salto[0]))
			return salto[1]

	
	def setObstaculo(self):
		self.obstaculos = Graficos.LogicaObstaculo.crearObstaculo(self.obstaculos)
		print(len(self.obstaculos))

	def pintarObstaculo(self):
		self.setObstaculo()

		for element in self.obstaculos:
			Graficos.ventana.blit(Graficos.CONO,element)

		self.obstaculos = Graficos.LogicaObstaculo.moverObstaculo(self.obstaculos)

		