from scipy.spatial import distance

class AspectoDelOjo:
	
	#Se define la formula eyeAspect radio, la cual recibe como parametros 
	#los 6 puntos del ojo, para posteriormente calcular la distancia entre
	#los puntos p2,p6 , la distancia entre los puntos p3,p5, la distancia 
	# entre los puntos p1, p4. Posteriomente se lleva a cabo el algoritmo 
	#propuesto por Tereza Soukupova y se obtiene el valor del  
	#EAR (Eye Aspect Ratio)

	#Se define la constante que sera el valor de referencia para el aspecto de los ojos.
	aspectoDeOjos = 190

	def calcularAspectoDelOjo(self,p1,p2,p3,p4,p5,p6):
	
		# Se calcula la distancia entre el punto 2 y el punto 6.
		p2_p6 = distance.euclidean(p2,p6)
	
		#Se calcula la distancia entre el punto 3 y el punto 5.
		p3_p5 = distance.euclidean(p3,p5)

		#Se calcula la distancia entre el punto 1 y el punto 4.
		p1_p4 = distance.euclidean(p1,p4)

		#Se calcula el valor del aspecto del ojo (EAR)

		ear =((p2_p6 + p3_p5)/2*p1_p4)

		#retorna el valor del aspecto del ojo (EAR)
		return ear
