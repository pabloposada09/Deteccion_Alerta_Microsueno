import cv2 as cv
import dlib
import AspectoDelOjo 
import BaseDeDatos
#import Alerta
from datetime import datetime
import Camara



class Microsueno:
	
	#Se cre un objeto de tipo Camara para poder usar los frames capturados y los atributos de la clase Camara
	global instanciaCamara
	instanciaCamara=Camara.Camara()

	#Se crea un objeto de la clase EyeAspectRatio y se usa la funcion
	#eyeAspectRatio
	global instanciaAdo
	instanciaAdo= AspectoDelOjo.AspectoDelOjo()
	
	#Se crea un objeto de tipo dlib, el cual nos permite identificar rostros en una imagen.
	global detector_de_rostros
	detector_de_rostros = cv.CascadeClassifier()
	detector_de_rostros.load(cv.samples.findFile("/home/pi/Desktop/Codigo_Version_2_Imutils/haarcascade_frontalface_alt2.xml"))

	#Se crea un objeto de tipo dlib, el cual nos permite ubicar 68 puntos en un rostro que se 
	#haya identificado previamente, este objeto utiliza un archivo que hace parte de la
	#documentacion de la libreria dlib.
	global predictor 
	predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

	#Se creo un objeto de tipo BaseDeDatos para guardar la fecha y la hora en la que se presenta el microsueño
	global instanciaBd
	instanciaBd = BaseDeDatos.BaseDeDatos()
	
	#Se crea un objeto de tipo Buzzer, para emitir la alerta cuando se detecte el microsueño.
	global instanciaAlerta	
	#instanciaAlerta = Alerta.Alerta()


	#Metodo para detectar si existe microsueño, recibo como parametro el objeto de tipi VideoCapture
	def detectarMicrosueno(self,cap):
		while True:
			
			
			#Se utiliza la funcion cap.read la cual devuelve un valor booleano que nos indica si fue posible leer correctamente el frame.
			#Si el frame es leido correctamente el valor que tomara la variable ret es true, de lo contrario sera false.
			frame = cap.read()

			# Se usa la funcion cvtColor, para convertir el frame de RGB a una escala de gris, que puede ser procesado de manera mas 
			#efectiva por parte de la CPU.
			gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
		
			if cv.waitKey(1) == ord('q'):
				break
			
			#Se detectan los rostros que se encuentran en el frame gray.	
			rostrosDetectados = detector_de_rostros.detectMultiScale(gray)
	                
	
                        #Se convierte la tupla de rostros detectados en un arreglo de que pueda ser utilizado por dlib.
			for (x,y,w,h) in rostrosDetectados:
				rostrosDetectadosDlib = dlib.rectangle(int(x), int(y), int(x+w), int(y+h))
                        
				
		
				#Se para como parametro el objeto rostros ya que se compone de 
				#4 elementos, los cuales son las coordenadas, con las cuales 
				#se puede dibujar un cuadro alrededor del rostro y a su vez son 
				# necesarias para que se puedan ubicar los puntos de referencia 
				#o "landmarks" en el rostro.
				puntosDeReferencia = predictor(gray,rostrosDetectadosDlib)
		
				#Se definen las 6 coordenadas que son necesarias para calcular
				#el aspecto de cada ojo, esto se hace con los 68 puntos de refencia
				#que obtuvimos gracias a la formula predictor(grady,rostros)
			
				#Coordenadas de los puntos del ojo izquierdo
				p1Izq = (puntosDeReferencia.part(36).x,puntosDeReferencia.part(36).y)
				p2Izq = (puntosDeReferencia.part(37).x,puntosDeReferencia.part(37).y)
				p3Izq = (puntosDeReferencia.part(38).x,puntosDeReferencia.part(38).y)
				p4Izq = (puntosDeReferencia.part(39).x,puntosDeReferencia.part(39).y)
				p5Izq = (puntosDeReferencia.part(40).x,puntosDeReferencia.part(40).y)
				p6Izq = (puntosDeReferencia.part(41).x,puntosDeReferencia.part(41).y)
	
			
	
				#Coordenadas de los puntos del ojo derecho
				p1Der = (puntosDeReferencia.part(42).x,puntosDeReferencia.part(42).y)
				p2Der = (puntosDeReferencia.part(43).x,puntosDeReferencia.part(43).y)
				p3Der = (puntosDeReferencia.part(44).x,puntosDeReferencia.part(44).y)
				p4Der = (puntosDeReferencia.part(45).x,puntosDeReferencia.part(45).y)
				p5Der = (puntosDeReferencia.part(46).x,puntosDeReferencia.part(46).y)
				p6Der = (puntosDeReferencia.part(47).x,puntosDeReferencia.part(47).y)	

				
				#Se calcula el aspecto del ojo (ADO), del ojo izquierdo
				adoIzq = instanciaAdo.calcularAspectoDelOjo(p1Izq,p2Izq,p3Izq,p4Izq,p5Izq,p6Izq)
					
				#Se calcula el aspecto del ojo (ADO), del ojo derecho
				adoDer = instanciaAdo.calcularAspectoDelOjo(p1Der,p2Der,p3Der,p4Der,p5Der,p6Der)
	
			
				#Se lleva a cabo un promedio del ADO de ambos ojos.
				adoTotal = (adoIzq+adoDer)/2
				print (adoTotal)
		
				#Se verifica si el earTotal es menor que la constante de refencia que definimos 
				#como aspectoDeOjos, de ser asi hace un incremento en la variable contador.
				if adoTotal < instanciaAdo.aspectoDeOjos:
					contadorDeFrames +=1
					
					# Si la variable contador iguala o supera la constante framesConsecutivos
					# se emite una alerta sonora y visual al conductor y aumenta en 1 la variable
					#microsueno y la variable contador vuelve a ser 0.
					if contadorDeFrames >= instanciaCamara.framesConsecutivos:
						
						#Se crea una objeto de tipo datetime para poder determinar la hora y fecha 
						#en la que se presento el microsueño
						informacion =datetime.now()
						
						#Se convierte el ano, el mes y el dia a string y luego
						#se organiza la informacion de la fecha en el formato yyyy/mm/dd y se almacena en la variable fecha
						fecha =str(informacion.year)+"/"+str(informacion.month)+"/"+str(informacion.day)
						
						#Se convierte la hora, minuto y segundo a string,
						#luego se organizar en el formato hh:mm:ss y posteriormente se almacena en la variable hora
						hora=str(informacion.hour)+":"+str(informacion.minute)+":"+str(informacion.second)
						
						#Se inserta por medio de la instancia instanciaBaseDeDatos la hora y fecha del microsueno
						instanciaBd.insertarRegistro(hora,fecha)	
						print ("Microsueno")
						print ("Emitiendo Alerta Sonora")
						print ("Emitiendo Alerta Visual")
						print ("Almacenando en la base de datos")
						print ("Los ultimos registros de la base de datos son")
						
						instanciaBd.leerTabla()
						
						#Se utiliza la instanciaBuzzer para emitir la alerta
						#instanciaAlerta.emitirAlerta()
						
						contadorDeFrames=0
				else: 
					#Se vuelve a poner la variable contador en 0 ya que puede que tomara los ojos cerrados
					#solamente en 1 frame.
					contadorDeFrames=0
				
		
			cv.imshow('Frame',frame)
	
