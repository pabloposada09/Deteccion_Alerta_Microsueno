from imutils.video import VideoStream


class Camara:

	

	#Se define la constante que sera el valor de refencia de la cantidad de frames, para indicar
	#la presencia de un microsueno.
	framesConsecutivos = 7

	#Se define la variable que nos indicara la cantidad de frames que el conductor estuvo
	#con los ojos cerrados
	#contadorDeFrames = 0


	#Metodo en el cual se abre la camara
	
	def abrirCamara(self):
	
		#Se crea un objeto de tipo VideoCapture, con el parametro 0, que indica que se esta utilizando la camara por defecto.
		cap= VideoStream(src=0).start()
		
		return cap
		
	
	
	