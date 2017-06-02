import pygame
from logica.LogicaCamino import LogicaCamino
from logica.LogicaJugador import LogicaJugador
from logica.LogicaDificultad import LogicaDificultad
from logica.LogicaObstaculo import LogicaObstaculo
from logica.LogicaBillete import LogicaBillete
from logica.LogicaPuntaje import LogicaPuntaje

class Graficos(object):
	
	""" Esta clase controla toda la parte grafica del juego"""
	pygame.init()
	
	ventana = pygame.display.set_mode((640,384))

	""" Objetos """
	LogicaCamino = LogicaCamino(0)
	LogicaJugador = LogicaJugador(16)
	LogicaObstaculo = LogicaObstaculo()
	LogicaBillete = LogicaBillete()
	LogicaPuntaje = LogicaPuntaje()

	"""Fuentes"""
	FUENTE = pygame.font.Font("recursos/fuentes/orange_juice.ttf",40)
	FUENTE2 = pygame.font.Font("recursos/fuentes/Jelly_Crazies.ttf",15)
	FUENTE3 = pygame.font.Font("recursos/fuentes/Jelly_Crazies.ttf",30)

	PERDISTE = FUENTE3.render('PERDISTE', True, (200,100,100))
	PUNTAJE = FUENTE2.render('PUNTAJE', True, (250,250,250))
	PUNTAJEMAX = FUENTE2.render('TU RECORD', True, (250,250,250))

	""" Imagenes que va a utilizar el juego"""
	LOGO = pygame.image.load("recursos/botones/logo.png")
	VACIO = pygame.image.load("recursos/botones/vacio.png")
	CONFIGURAR = pygame.image.load("recursos/botones/configurar.png")
	PAUSA = pygame.image.load("recursos/botones/pausa.png")
	TRANSPARENTE = pygame.image.load("recursos/fondo/gris.png")

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
		self.sprites_Logo = [Graficos.LOGO, Graficos.VACIO]
		self.obstaculos = [(640,296)]
		self.billetes = [(650,140)]
		self.puntaje = 0
		self.maxpuntaje = 0
		self.spr = 0
		self.sprvel = 30
		self.colisionObstaculo = False
		self.colisionBillete = False
	
	def pintarLogo(self, click):
		if click:
			sprite = self.sprite()
			Graficos.ventana.blit(self.sprites_Logo[sprite],(192,128))	
		else:
			Graficos.ventana.blit(self.sprites_Logo[0],(192,128))
		
		Graficos.ventana.blit(Graficos.CONFIGURAR,(600,8))

	def sprite(self):
		if self.sprvel == 0:
			if self.spr == 0:
				self.spr += 1
			elif self.spr == 1:
				self.spr = 0
			self.sprvel = 30
		else:
			self.sprvel -= 1

		return self.spr

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

		elif self.estado == 3:
			Graficos.ventana.blit(Graficos.CAMINO,(0,128))

	def pintarPuntaje(self):
		self.puntaje, self.maxpuntaje = Graficos.LogicaPuntaje.getPuntaje(self.colisionObstaculo)
		score = Graficos.FUENTE2.render(str(self.puntaje), True, (255,255,255))
		Graficos.ventana.blit(score,(10,10))

	def pintarPersonaje(self, saltar):
		if saltar == False:
			sprite = Graficos.LogicaJugador.getSprite()
			Graficos.ventana.blit(self.sprites_Jugador[sprite], (32,200))
		elif saltar == True:
			salto = Graficos.LogicaJugador.getSalto()
			Graficos.ventana.blit(self.sprites_Jugador[5], (32,salto[0]))
			return salto[1]

	def pintarObstaculo(self):
		""" Llama al metodo de la clase LogicaObstaculo y crear una tupla con la posicion en 'x' y 'y' y se agrega a una lista con todas las posiciones de cada obstaculo"""
		self.obstaculos = Graficos.LogicaObstaculo.crearObstaculo(self.obstaculos)

		"""Este ciclo se encarga de recorrer la lista e imprimir el obstaculo"""
		for element in self.obstaculos:
			Graficos.ventana.blit(Graficos.CONO,element)

		"""Se modifica la lista restandole a la posicion en 'x' de cada tupla y hace que el obstaculo se mueva"""
		self.obstaculos = Graficos.LogicaObstaculo.moverObstaculo(self.obstaculos)

		"""Se encarga de eliminar los obtaculos cuya posicion en 'x' se pasa del limite"""
		self.obstaculos = Graficos.LogicaObstaculo.borrarObstaculo(self.obstaculos)


	def pintarBillete(self):
		sprite = Graficos.LogicaBillete.getSprite()

		self.billetes = Graficos.LogicaBillete.crearBillete(self.billetes)

		for element in self.billetes:
			Graficos.ventana.blit(self.sprites_Billete[sprite],element)

		self.billetes = Graficos.LogicaBillete.moverBillete(self.billetes)

		self.billetes = Graficos.LogicaBillete.borrarBillete(self.billetes)

	def colisiones(self):
		self.colisionObstaculo = Graficos.LogicaJugador.colisionObstaculo(self.obstaculos)

		if self.colisionObstaculo:
			return True
		else:
			return False

	def pintarFiltro(self):
		Graficos.ventana.blit(Graficos.TRANSPARENTE,(0,0))

	def pintarPerdiste(self):
		Graficos.ventana.blit(Graficos.PERDISTE,(150,80))

	def puntajeFinal(self):
		score = Graficos.FUENTE3.render(str(self.puntaje), True, (255,255,255))
		scoremax = Graficos.FUENTE3.render(str(self.maxpuntaje), True, (255,255,255))

		Graficos.ventana.blit(Graficos.PUNTAJE,(240,160))
		Graficos.ventana.blit(score,(295,190))
		Graficos.ventana.blit(Graficos.PUNTAJEMAX,(220,280))
		Graficos.ventana.blit(scoremax,(295,310))

