#Fragmento de codigo al cual se le asignan una o varias tareas al cual se le debe agregar un nombre y se le deben colocar valores conocido como parametros para procesarlos en la funcion aunque esto ultimo no es obligatorio y si no regresamos un valor nos regresara "none"

"""
def funcion(num1,num2):
	print num1 + num2

funcion(3,4)#Esto son los argumentos de la funcion esto llama a la funcion y la ejecuta 
"""
"""
def funcion(cad, v=2, *algomas): #El asterisco al lado de algo mas sirve para que el resto de cadenas o cosas que esten ahi se almacenen en tuplas
	print cad * v
	for cadena in algomas:
		print cadena * v 

funcion("Python",5,"Hola","Adios","N","cadenas")	
"""
"""
def funcion(cad, v=2, **algomas): #al usar dos asteriscos se convierte en diccionarios en vez de en tuplas
	print cad * v
	 
	print algomas["cadenaextra"]
	print algomas["cadenademas"]
funcion("Python",5,cadenaextra = "Hola",cadenademas = "Adios")
"""

def funcion(num1,num2): 
	return num1 + num2
	

resultado_de_suma = funcion(3,4)

print resultado_de_suma