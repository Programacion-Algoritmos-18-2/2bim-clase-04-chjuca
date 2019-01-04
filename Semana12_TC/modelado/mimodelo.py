import codecs								# Importamos las librerias Ncesarias
import sys
		
class Equipo(object):						# Creamo una Clase Equipo
	def __init__(self, nombres,ciudad,campeonatos,numero):		#Constructor de la Clase Equipo	quipo
		self.nombres = nombres									# Atributos de la clase
		self.ciudad = ciudad
		self.campeonatos = int(campeonatos)
		self.numJugadores = int(numero)

	def setNombre(self,nombres):						# Metodo set de la Clase
		self.nombres = nombres

	def setCiudad(self,ciudad):
		self.ciudad = ciudad

	def setCampeonatos(self,campeonatos):
		self.campeonatos = int(campeonatos)

	def setNumJugadores(self,numero):
		self.numJugadores = int(numero)

	def getNombre(self):							# Metodos get de la Clase
		return self.nombres

	def getCiudad(self):
		return self.ciudad

	def getCampeonatos(self):
		return self.campeonatos

	def getNumJugadores(self):
		return self.numJugadores

	def __str__(self):							# Metodo __str__para presentar la informacion de la clase
		return "- Nombre: %s\n-Ciudad: %s\n-Campeonatos: %d\n-Numero de Jugadores: %d\n\n"%(self.getNombre(),self.getCiudad(),self.getCampeonatos(),self.getNumJugadores())

	def __repr__(self):							# Metodo __repr__ para presentar la informacion frente a otra funcion 
		return "- Nombre: %s\n-Ciudad: %s\n-Campeonatos: %d\n-Numero de Jugadores: %d\n\n"%(self.getNombre(),self.getCiudad(),self.getCampeonatos(),self.getNumJugadores())


class MiArchivo():						# Clase MiArchivo
	def __init__(self):					# Constructor de la clase
		self.archivo = codecs.open("informacion.csv","r")	# archivo abre el documento csv en modo read

	def obtener_informacion(self):			# Se lee las lineas del arrchivo
		return self.archivo.readlines()

	def cerrar_archivo(self):				# Se cierra el Archivo
		self.archivo.close()

class MiArchivoEscribir():				# Creacion de la clase MiArchivoEscribir

    def __init__(self):					# Constructor de la clase
        self.archivo = codecs.open("informacion_ordenada.csv", "a")	  # archivo abre el documento csv en modo write

    def agregar_informacion(self, p):				# Metodo que permite la escritura en un nuevo documento
        self.archivo.write("-Nombre: %s\n-Ciudad: %s\n-Campeonatos: %d\n-Numero de Jugadores: %d\n\n"%(p.getNombre(),p.getCiudad(),p.getCampeonatos(),p.getNumJugadores()))

    def cerrar_archivo(self):				# Metodo que permite cerrar el archivo
        self.archivo.close()

class Operaciones(object):					# Creacion de la clase Operaciones
    
    def __init__(self, listado):			# Constructor de la clase Operaciones
        self.listado_equipos = listado 		# Atributo de la clase

    def ordenarNombre(self):				# Metoodo que permite Ordenar la lista de objetos segun el Nombre
        return sorted(self.listado_equipos, key=lambda e: e.getNombre())

    def ordenarCampeonatos(self):			# Metoodo que permite Ordenar la lista de objetos segun los Campeonatos
        return sorted(self.listado_equipos, key=lambda e: e.getCampeonatos())