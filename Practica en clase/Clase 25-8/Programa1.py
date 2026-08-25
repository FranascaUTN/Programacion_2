

#Creamios la clase persona, el nombre se escribe en PascalCase
class Persona:
    pass


#Creamos Objetos de la clase persona
persona1 = Persona()
persona2 = Persona()
persona3 = Persona()



class Producto:
    # Siempre dos guiones adelante y dos atras en init
    def __init__(self, nombre, precio, vencimiento):
        self.nombre = nombre
        self.precio = precio
        self.vencimiento = vencimiento



pan = Producto ("Pan", 500, "01/01/2027")
leche = Producto ("Leche", 800, "16/01/2026")

print (f"{pan.nombre}: ${pan.precio} y vence el {pan.vencimiento}")
print (f"{leche.nombre}: ${leche.precio}")
