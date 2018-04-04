d = {'Clave1':[1,2,3],#Para las claves se puede poner cualquier tipo de dato a excepcion de listas y diccionarios
	 4:True
}#los diccionarios no tienen indices y para leerlos se usan las claves no es como las listas que se leen con indice("[2:0]")eso es un indice

d[4] = False #Tambien se puede cambiar por una cadena de texto por ejemplo "Hola"

print d[4] #es importante poner la clave inclusive la clave puede ser un 4
#y a diferencia de las tuplas si se pueden cambiar los valores lo que no se peuden cambiar son las claves
