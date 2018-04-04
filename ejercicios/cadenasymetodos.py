#una cadena tambien es un objeto las listas las tuplas y los diccionarios tambien , cadenas y listas pertenecen a un objeto llamado secuencia
"""
s = "Hola Mundo"

print len(s)#len permite obtener el numero de caracteres que ofrece esa cadena
"""
"""
s = "Hola oMounodoo"

print s.count("o",5) #el .count cuenta el numero de cosas que tenga el objeto y se le puede decir de donde a donde buscarcuanta el valor el inicio y el fin de mi objeto
"""
"""
s = "Hola Mundo"

print s.lower()#Poner las letras en minusculas

print s.upper()#Poner las letras en Mayusculas
"""
"""
s = "Hola Mundo"

print s.replace("Hola","x",1)# el uno dice que solo lo haga con la primera coincidencia esto reemplaza las o por equiz #el replace permite cambiar un caracter o una cadena completa por otra cadena o caracter
"""
"""
s = "Hola Mundo"

print s.split("o",1)#el uno es para que se ejecute con la primera coincidencia Regresa una lista conteniendo las subcadenas que se generan a partir de dividir la cadena cada que encuentre el caracter que le ponemos entre los parentecis como un argumento de nuestro metodo
"""
"""
s = "Hola Mundo"

print s.find("a")#tambien se le puede dar el inicio y el fin Sirve para encontrar un valor dentro de nuestro objeto y nos regresa un entero con la ubicacion de la coincidencia o sea en el caso de Hola mundo regresa un 3 si buscamos la a y si en vez de find se coloca rfind lo busca de atras para adelante
"""

t = ("H","o","l","a")
s = ";"

print s.join(t) #Devuelve una cadena con todos los caracteres separados por el objeto que se denomina en "s"

#para saber el tipo de objeto se usa el comando type por ejemplo type(s.join(t))