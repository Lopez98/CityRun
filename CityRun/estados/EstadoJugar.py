from graficos.Graficos import Graficos

Graficos = Graficos(2)

class EstadoJugar(object):

	""" Estado en el que empieza el juego"""
	
	def __init__(self):
		Graficos.pintarFondo()
		Graficos.pintarCamino()
		Graficos.pintarObstaculo()
		Graficos.pintarBillete()
		Graficos.pintarPuntaje()	

	def correr(self):
		Graficos.pintarPersonaje(False)

	def saltar(self):
		return Graficos.pintarPersonaje(True)
