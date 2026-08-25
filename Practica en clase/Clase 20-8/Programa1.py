#Creacion de una lista vacia
cuadrados = []

#Usamos for que vaya del 1 al 10
for numero in range(1,11):
    #Guardo en la lista los resultados de la potencia
    cuadrados.append(numero ** 2)

#Imprimo la lista (For automatico)
print(cuadrados)

# ----------------------------------------
# --------- Otra forma de hacerlo --------
# ----------------------------------------
# Expresion for elemento in coleccion

cuadrados_comp = [numero ** 2 for numero in range(1, 11)]
print(cuadrados_comp)
