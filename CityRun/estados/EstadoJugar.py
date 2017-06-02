from graficos.Graficos import Graficos


class EstadoJugar(object):

	""" Estado en el que empieza el juego"""

	Graficos = Graficos(2)
	
	def __init__(self):
		EstadoJugar.Graficos.pintarFondo()
		EstadoJugar.Graficos.pintarCamino()
		EstadoJugar.Graficos.pintarObstaculo()
		EstadoJugar.Graficos.pintarBillete()
		EstadoJugar.Graficos.pintarPuntaje()
		self.colision = EstadoJugar.Graficos.colisiones()	

	def correr(self):
		EstadoJugar.Graficos.pintarPersonaje(False)
		return self.colision

	def saltar(self):
		return EstadoJugar.Graficos.pintarPersonaje(True),self.colision
		
