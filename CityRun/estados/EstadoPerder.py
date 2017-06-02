from graficos.Graficos import Graficos
from estados.EstadoJugar import EstadoJugar

Graficos = EstadoJugar().Graficos

class EstadoPerder(object):

	"""Se encarga de mostrar el puntaje final de la partida y la opcion de reiniciar el juego o salir"""

	def __init__(self):
		Graficos.pintarFondo()
		Graficos.pintarCamino()
		Graficos.pintarFiltro()
		Graficos.pintarPerdiste()
		Graficos.puntajeFinal()

		