import codecs
import sys

class Equipo(object):
	def __init__(self, nombres,ciudad,campeonatos,numero):
		self.nombres = nombres
		self.ciudad = ciudad
		self.campeonatos = int(campeonatos)
		self.numJugadores = int(numero)

	def setNombre(self,nombres):
		self.nombres = nombres

	def setCiudad(self,ciudad):
		self.ciudad = ciudad

	def setCampeonatos(self,campeonatos):
		self.campeonatos = int(campeonatos)

	def setNumJugadores(self,numero):
		self.numJugadores = int(numero)

	def getNombre(self):
		return self.nombres

	def getCiudad(self):
		return self.ciudad

	def getCampeonatos(self):
		return self.campeonatos

	def getNumJugadores(self):
		return self.numJugadores

	def __str__(self):
		return "- Nombre: %s\n-Ciudad: %s\n-Campeonatos: %d\n-Numero de Jugadores: %d\n\n"%(self.getNombre(),self.getCiudad(),self.getCampeonatos(),self.getNumJugadores())

	def __repr__(self):
		return "- Nombre: %s\n-Ciudad: %s\n-Campeonatos: %d\n-Numero de Jugadores: %d\n\n"%(self.getNombre(),self.getCiudad(),self.getCampeonatos(),self.getNumJugadores())


class MiArchivo():
	def __init__(self):
		self.archivo = codecs.open("informacion.csv","r")

	def obtener_informacion(self):
		return self.archivo.readlines()

	def cerrar_archivo(self):
		self.archivo.close()

class MiArchivoEscribir:

    def __init__(self):
        self.archivo = codecs.open("informacion_ordenada.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write("- Nombre: %s\n-Ciudad: %s\n-Campeonatos: %d\n-Numero de Jugadores: %d\n\n"%(p.getNombre(),p.getCiudad(),p.getCampeonatos(),p.getNumJugadores()))

    def cerrar_archivo(self):
        self.archivo.close()

class Operaciones(object):
    
    def __init__(self, listado):
        self.listado_equipos = listado

    def ordenarNombre(self):
        return sorted(self.listado_equipos, key=lambda e: e.getNombre())

    def ordenarCampeonatos(self):
        return sorted(self.listado_equipos, key=lambda e: e.getCampeonatos())