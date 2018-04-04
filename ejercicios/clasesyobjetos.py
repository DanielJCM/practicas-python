#Objetos: caracteristicas del objeto en el que nos orientamos a sus caracteristicas las cuales se llaman atributos y sus acciones que se llaman metodos
#Clases plantillas o moldes en el cual se establecen los atributos de nuestro objeto

class Humano:
	def __init__(self,edad):#funcion que al estar dentro de una clase se vuelve metodo 
		self.edad = edad
	#EL init siempre va en una clases y siempre se le pone self y es para que se guarde lar eferencia al objeto que estoy creando


	def hablar(self,mensaje):#El self es porque al ejecutar el metodo de pedro que guarda una instancia de la clase humana python enviara una referencia a pedro y podra acceder a todos los atributos que se tengan dentro de ese objeto
			print mensaje

pedro = Humano(26)

raul = Humano(21)

print "Soy Pedro y tengo ", pedro.edad
print "Soy raul y tengo", raul.edad
pedro.hablar("Hola")

raul.hablar("Hola, Pedro")