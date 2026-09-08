from validaciones import validar_nombre


class Persona:
    #Constructor
    def __init__(self, nombre, apellido):
        self.nombre = validar_nombre(nombre)
        self.apellido = validar_nombre(apellido)

    #Salida del print
    def __str__(self):
        return (
            f"Mi nombre es {self.apellido.upper()}, "
            f"{self.nombre.title()}"
        )

"""
p1 = Persona("Sergio Adrian", "Maldonado")
print (p1)
"""

"""Otro ejemplo incluyendo herencia y validaciones"""

class Vehiculo:

    def __init__ (self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def prender(self):
        print("Estoy prendido") 

    def apagar(self):
        print("Estoy apagado")

    def __str__(self):
        return f"Soy de color {self.color} y tengo {self.ruedas} ruedas"


class Motos(Vehiculo):
    pass


class Auto(Vehiculo):

    def __init__(self, color, ruedas, ejes, puertas):
        super().__init__(color, ruedas)
        self.puertas = puertas
        self.ejes = ejes

    def abrir_puerta(self):
        print("Abri puerta")

    def cerrar_puerta(self):
        print("Cerre puerta")

    def __str__ (self):
        return (
            f"Tengo {self.ruedas} ruedas y soy {self.color}. "
            f"Tambien tengo {self.ejes} ejes y {self.puertas} puertas"
        )
            

# ---------------------------------------------------------

mi_auto = Auto("azul", 4, 2, 5)
print (mi_auto)