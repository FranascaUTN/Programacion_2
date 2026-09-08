

class Empleado:
    """Empleado con nomvre y presentacion basica"""

    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print (f"Soy {self.nombre}")


class Gerente (Empleado):
    """Empleado que ademas dirige un equipo"""

    def __init__(self, nombre, equipo):
        super().__init__(nombre)
        self._equipo = equipo

    def presentarse(self):
        """Se extiende la presentacion del padre con la del hijo"""

        super().presentarse()
        print(f"y dirijo un equipo de {len(self._equipo)} personas")

