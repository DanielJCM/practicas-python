#Permiten ejecutar cierto codigo n veces dependiendo de una condicion y hasta que esa condicion cambie
"""
while True:
	print "Hola"
Bucle infinito porque no se detiene
"""
"""
edad = 0

while edad <= 20:

	if edad == 15:
		edad = edad + 1
		continue #La palabra continue es para que se salte esa parte del codigo

	print "Tienes: " + str(edad)
	edad = edad + 1
"""
"""
edad = 0

while edad <= 20:

	if edad == 15:
		
		break #Hace que el programa termine

	print "Tienes: " + str(edad)
	edad = edad + 1

"""
#Bucle para recorrer listas o tuplas

lista = ["Elemento 1","Elemento 2","Elemento 3"]

"""
for cosa in lista: #Cosa es para que se guarden los elementos que hay en la otra variable
	print cosa 
"""

#Imprime los caracteres de la cadena porque las cadenas son de tipo secuencia en python
for letra in "Cadena":
	print letra 
