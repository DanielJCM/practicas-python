class Humano:
	def __init__(self,edad):
		self.edad = edad


	def hablar(self,mensaje):
			print mensaje

class IngSistemas(Humano): #Hereda de la clase humano
	def __init__(self):
		print "Hola"

	def programar(self,lenguaje):
		print "Voy a programar en ", lenguaje

class LicDerecho(Humano):#Hereda de la clase humano
	def __init__(self,escuela):
		print "Lic. en Derecho egresado de: ", escuela
	def estudiarCaso(self,de):
		print "Debo estudiar el caso de ", de

class estudioso(LicDerecho, IngSistemas):#el orden de las clases importara solo si en alguna de esas clases hay un metodo init ya que eso hace que si alguno tiene un init toma es el init de esa primera clase
	pass #pass sirve o significa como vete, no hay nada mas que hacer aqui 

pepe = estudioso("ULA")

pepe.hablar("Hola, soy de herencia multiple")

pepe.programar("Python")

pepe.estudiarCaso("Juan")