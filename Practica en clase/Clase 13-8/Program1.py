"""
Ejercicios Integradores. Punto 1 :
Pedir un número y mostrar si es par o impar (usando el operador módulo %). 
Funciones sugeridas: isdigit()
"""
respuesta = input("Ingrese un numero: ")

#Con .isdigit() confirmamos que el usuario ingreso un numero
if not respuesta.isdigit() :
    print("Error en el valor ingresado")
else :
    #Convertimos lo ingresdo en un numero
    respuesta = int(respuesta)

    #Confirmamos que sea Par
    if respuesta % 2 == 0 :
        print("El numero es Par")
    else:
        print ("El numero es Impar")
