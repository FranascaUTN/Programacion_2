"""
Ejemplos de la clase: Listas
"""

notas = [3, 4, 7, 10, 2]

#El print Itera entre los elementos solo
print (notas)

#En la posicion 2 inserta un 3
notas.insert(2,3)

#Agrega al final un 4
notas.append(4)

#Elimina el ultimo elemento, si le pones un indice elimina el de la posicion indicada
notas.pop()

#El string es una lista
letras = list("hola mundo")
print(letras)

#len devuelve la cantidad de valores en la lista
print(len(notas))

#Imprime los elementos en la sposiciones del rango, no imprime el extremo superior, sino el anterior
print(notas[1:3])
