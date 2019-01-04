from modelado.mimodelo import *						# Se importa todas las clases del modulo mimodelo
m = MiArchivo()										# Creamos un objeto tipo Archivo
m2 = MiArchivoEscribir()							# Creamos un Objeto tipo MiArchivoEscribir

lista = m.obtener_informacion()						# Creamos una lista con la infoamcion leida
lista = [l.split("|") for l in lista]				# Separamos la lista por el caracter "|"
	
lista_equipos=[]								# Creamos uns lista vacia
for i in lista:									
    e = Equipo(i[0], i[1], i[2], i[3])			# Creamos un Objeto de tipo Equipo
    lista_equipos.append(e)						# Añadimos un elemento al final de la lista 

op = Operaciones(lista_equipos)					# Creamos un objeto tipo Operacion  

opt=input("Desea Ordenar la lista de Equipos por Nombre o Campeonatos(N/C)?  ")		# Mostramos un mensaje en pantalla

if opt=='N' or opt=='n':						# Condicion para evaluar el valor ingresado
	lista_ordenada=op.ordenarNombre()			# Se llama a la funcion OdernarNombre
else:
	lista_ordenada=op.ordenarCampeonatos()		# Se llama a la funcion OrdenarCampeonatos

for i in lista_ordenada:
	m2.agregar_informacion(i)					# Se agrega el objeto a la lista
	print(i)									# Se presenta la infoamcion del Objeto

m.cerrar_archivo()								# Cerramos ambos archivos
m2.cerrar_archivo()