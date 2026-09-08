

class Animal:
    """Clase padre"""

    def respirar(self):
        """Imprime que el animal esta respirando"""
        print("Respirando... ")


class Perro(Animal):
    """Hijo de animal"""
    """Perro que hereda todo sin agregar comportaminetos"""
    pass


pichicho = Perro()
pichicho.respirar()

#Demostramos que pichicho es instancia de perro y tambien de animal
print (isinstance(pichicho, Perro)) 
print (isinstance(pichicho, Animal))
print (isinstance(pichicho, object))
