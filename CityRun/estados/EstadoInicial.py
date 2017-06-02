from graficos.Graficos import Graficos

Graficos = Graficos(1)

class EstadoInicial(object):

	""" Este es el primer estado del juego. Muestra la pantalla de bienvenida"""

	def __init__(self, click):
		Graficos.pintarFondo()
		Graficos.pintarCamino()
		Graficos.pintarLogo(click)
