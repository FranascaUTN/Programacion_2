
def es_primo(n):
    # Si es menor a dos no e sprimo
    if n < 2:
        return False

    #Entre 2 y el numero a chequear si es primo
    for divisor in range(2, n):
        #Lo voy dividiendo y si es divisible por alguno retorno falso
        if n % divisor == 0:
            return False
    # Si no fue dividible por ninguno de los numeros de entre 2 y n-1 retornamos verdadero
    return True

#Para todo numero en el rango (de 2 a 50)
for numero in range(2, 51):
    if es_primo(numero):
        print(numero, end=" ")