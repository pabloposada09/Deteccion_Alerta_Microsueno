import sqlite3

from sqlite3 import Error

class BaseDeDatos:

	#Se crea la funcion, para realizar la conexion con la base de datos.	
	#def conexionBaseDeDatos(self):
	
	#	try:

			#Se realiza la conexion con la base de datos, de no existir, esta se crea.
	#		conexion= sqlite3.connect('microsueno.db') 
	#		cursor = conexion.cursor()
	#		print ("Se creo")
			
			
			#Se retorna la conexion para poder usarla en los otros metodos, para crear tablas y modificarlas.
	#		return conexion
	#	except Error:

	#		print(Error)



	def insertarRegistro(self,hora,fecha):
		try:
			conexion = sqlite3.connect('microsueno.db')
		except Error:	
			print(Error)
	
		#se crea un objeto de tipo cursor, para poder ejecutar Sentencias de SQL
		cursor= conexion.cursor()

		
		# se insertar en la tabla por medio de la sentencia SQL
		cursor.execute("INSERT INTO microsueno(Hora,Fecha) VALUES (?,?);",(hora,fecha))
		#Se guardan los cambios realizados en la tabla.
		conexion.commit()		
		
		conexion.close()



	# CODIGO DE AQUI EN ADELANTE ES SOLO PARA PRUEBAS


	
	def crearTabla(self):
		try:
			conexion =sqlite3.connect('microsueno.db')
		
		except Error:
			print(Error)
 
		
		# Se crea un objeto de tipo cursor, para poder ejecutar Sentencias de SQL.
		cursor = conexion.cursor()
		
		#Se crea la tabla microsueno
		cursor.execute("CREATE TABLE if not exists microsueno(id INTEGER PRIMARY KEY,Hora TEXT NOT NULL, Fecha TEXT NOT NULL);")


	#Se crea este metodo para realizar pruebas
	def leerTabla(self):
		try:
			conexion =sqlite3.connect('microsueno.db')
                
		except Error:  
			print(Error)
		
		cursor=conexion.cursor()
		
		info = cursor.execute("SELECT id,Hora,Fecha FROM microsueno WHERE id > 34;")
		
		for registro in info: 
		
			print(registro)

	def eliminar(self, conexion):
		cursor=conexion.cursor()

		cursor.execute('DROP table if exists microsueno;')
	
