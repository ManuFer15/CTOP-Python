##Ejemplo 2
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self._edad = edad
        self.__dni = dni
p = Persona("Luis", 30, "12345678A")

print(p._edad)
print(p._Persona__dni)
