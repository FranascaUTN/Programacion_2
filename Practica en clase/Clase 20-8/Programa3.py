frase = input("Frase: ")
# La funcion .isalpha te indica si es o no un caracter alfabetico y si es lo bguarda en la nueva lista
letras = [c for c in frase if c.isalpha()]

print(letras)
print(f"Hay {len(letras)} letras en total")

# Siquisieramos que no se repitan los caracteres dentro de la nueva lista
# simplemente deberiamos cambiar el tipo de estructura de una lista [] a un
# Set {} 