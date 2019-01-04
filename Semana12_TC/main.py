from modelado.mimodelo import *
m = MiArchivo()
m2 = MiArchivoEscribir()

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]
	
lista_equipos=[]
for i in lista:
    e = Equipo(i[0], i[1], i[2], i[3])
    lista_equipos.append(e)

op = Operaciones(lista_equipos)

opt=input("Desea Ordenar la lista de Equipos por Nombre o Campeonatos(N/C)?  ")
if opt=='N' or opt=='n':
	lista_ordenada=op.ordenarNombre()
else:
	lista_ordenada=op.ordenarCampeonatos()

for i in lista_ordenada:
	m2.agregar_informacion(i)
	print(i)

m.cerrar_archivo()
m2.cerrar_archivo()