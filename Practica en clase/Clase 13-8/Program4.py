"""
Ejercicios Integradores. Punto 2 :
Pedir dos números y mostrar cuál de los dos es mayor. Si son iguales, mostrar "Son iguales". 
Funciones sugeridas: max()
"""
#La lectura siempre es e String
#Lectura de los numeros
numero_1 = input("Ingrese el primer numero: ")
numero_2 = input("Ingrese el segundo: ")

#Siempre confirmar que lo ingresado es valido
if not numero_1.isdigit() or not numero_2.isdigit() :
    print("Error, debe ingresar numeros..")
    #
else :
    #lo convierto de String a entero
    numero_1 = int(numero_1)
    numero_2 = int(numero_2)

    #Forma 1 de hacerlo: 
    if numero_1 > numero_2 :
        print (f"El primer numero ({numero_1}) es mayor al segundo ({numero_2}).")
        #
    elif numero_2 > numero_1 :
        print (f"El segundo numero ({numero_2}) es mayor al primero ({numero_1}).")
        #
    else :
        print ("Los numeros son iguales.")

    #Forma 2 de hacerlo:
    if numero_1 != numero_2 :
        print (f"El numero mayor es {max(numero_1, numero_2)}")
    else :
        print ("Los numeros son iguales. ")
    