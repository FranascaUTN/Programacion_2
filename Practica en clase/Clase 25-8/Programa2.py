

class Alumno:

    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def presentacion (self) :
        print (
            f"Mi nombre es {self.nombre}, tengo {self.edad} años"
            f" y mi promedio es {self.promedio}"
            )


alumno1 = Alumno ("Franco", 22, 7.0)
alumno1.presentacion()

