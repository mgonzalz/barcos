
"""Clase que contiene los atributos y los métodos estáticos"""
tablero_num_lineas = 10
tablero_num_columnas = 10

barcos_longitud = [2, 3, 3, 4, 4, 5]
'''
@staticmethod es un decorador que indica que el método no necesita de una instancia de la clase para ser llamado.
NO PERMITE ACCEDER A LOS ATRIBUTOS DE LA CLASE (self)
'''
@staticmethod
def generar_num_linea(x):
    return chr(65 + x) # 65 es el código ASCII de la letra; chr() devuelve de un entero el carácter correspondiente

@staticmethod
def generar_num_columna(y): # y es un entero
    return str(y)

@staticmethod
def generar_nombre_casilla(x, y, self):
    return self.generar_num_linea(x) + self.generar_num_columna(y) #Concatenacion: linea + columna
