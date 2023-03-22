from numpy import product
from ..juego import *
from Conventions import (
    tablero_num_lineas,
    tablero_num_columnas,
    generar_nombre_casilla
)
instances = {} # Diccionario de casillas
jugadas = set() # Conjunto de casillas jugadas, para poder comprobar si se ha hundido un barco.

''' REALIZACIÓN DE LAS CASILLAS'''

def __init__(self, x, y):
  # Adición de las coordenadas
  self.x = x
  self.y = y

def generar_nombre_casilla(self, x, y):
# Queremos poder acceder a una casilla a partir de sus coordenadas
  instances[x, y] = self
  
  # Generación del nombre de la casilla

  self._generar_nombre()

  # Queremos poder acceder a una casilla a partir de su nombre
  instances[self.nombre] = self
  
  # Evolución de la casilla
  self.jugada = False
  self.barco = None  # No toca a un barco de momento.

def _generar_nombre(self):
  """Este método puede ser sobrecargado fácilmente"""
  self.nombre = generar_nombre_casilla(self.x, self.y)

def jugar(self):
  """Describe qué pasa cuando jugamos una casilla"""
  self.jugada = True
  self.jugadas.add(self)
  
  if self.barco is not None:
      if len(self.casillas - self.casillas_jugadas) == 0: #PROBAR SELF.CASILLAS
          print("Hundido !!")
      else:
          print("Tocado !")
  else:
      print("Agua !")


''' METODO DE CLASE: @classmethod
classmethod es un decorador que permite definir un método de clase.
'''


@classmethod
def generar_casillas():
  for x, y in product(range(tablero_num_lineas),
                      range(tablero_num_columnas)):
      Case(x, y)

def __str__(self):
  """Sobrecarga del método de transformación en cadena"""
  if not self.jugada:
      return CASO_NO_JUGADO
  elif self.barco is None:
      return CASO_AGUA
  return CASO_TOCADO
