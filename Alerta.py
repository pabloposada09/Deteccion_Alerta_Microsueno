import RPi.GPIO as GPIO
from time import sleep

class Alerta:
	
	def emitirAlerta(self):
		#Se crea la variable que nos determinara por cuanto tiempo suena el buzzer
		i = 0

		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		buzzer=23
		GPIO.setup(buzzer,GPIO.OUT)
	
		#Se crea un bucle para que el buzzer suene por 4 segundos
		while i<4:
			GPIO.output(buzzer,GPIO.HIGH)
			sleep(0.1) # Delay in seconds
			GPIO.output(buzzer,GPIO.LOW)
			sleep(0.1)
			i += 1

		GPIO.output(buzzer,GPIO.LOW)
	
