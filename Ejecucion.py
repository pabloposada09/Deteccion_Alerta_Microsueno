import Microsueno
import Camara
import BaseDeDatos

class Ejecucion:

	instanciaCamara = Camara.Camara()

	instanciaMicrosueno = Microsueno.Microsueno()


	instanciaMicrosueno.detectarMicrosueno(instanciaCamara.abrirCamara())
	
	#instancia= BaseDeDatos.BaseDeDatos()
	#instancia.crearTabla()
