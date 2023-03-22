
"""Clase que contiene los atributos y los métodos estáticos"""
tablero_num_lineas = 10
tablero_num_columnas = 10

barcos_longitud = [2, 3, 3, 4, 4, 5]
'''
@staticmethod es un decorador que permite definir un método estático, sirve para crear métodos que no necesitan de una instancia* de la clase para ser llamados.
no modificará el estado de la instancia ni de la clase


@classmethod es un decorador que permite definir un método de clase, sirve para crear métodos que no necesitan de una instancia* de la clase para ser llamados.

*Una instancia es un objeto que se crea a partir de una clase. Por ejemplo, si tenemos una clase llamada Perro, 
podemos crear tantos objetos Perro como queramos,
cada uno de ellos será una instancia de la clase Perro.
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
