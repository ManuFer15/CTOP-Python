'''crea una clase Animal que reciba como atributos: nombre(string) y chip(booleano)
Esta clase tendra 2 metodos:
- tiene_choip: devuelve el buleano chip
- hablar: metodo generico que se sobreescribira en las clases hijas

##Crea 2 clases derivadas de animal:
-Perro: cuyo constructor, ademas del nombre y elchip, recibe el argumento raza(string). El metodo hablar devolvera "!GUAU, GUAU!"
-Gato: cuyo constructor, ademas del nombre y el chip, recibe el argumento color(string). El metodo hablar devolvera "!MIAU, MIAU!"
'''
class Animal:
    def __init__(self, nombre, chip):
        self.nombre = nombre
        self.chip = chip

    def tiene_chip(self):
        return self.chip

    def hablar(self):
        pass
class Perro(Animal):
    def __init__(self, nombre, chip, raza):
        super().__init__(nombre, chip)
        self.raza = raza

    def hablar(self):
        return "!GUAU, GUAU!"
class Gato(Animal):
    def __init__(self, nombre, chip, color):
        super().__init__(nombre, chip)
        self.color = color

    def hablar(self):
        return "!MIAU, MIAU!"
# Ejemplo de uso
perro1 = Perro("Danko", True, "Pastor Alemán")
gato1 = Gato("Goku", False, "Negro")
print("El perro se llama:", perro1.nombre, "y su raza es:", perro1.raza)
print("El gato se llama:", gato1.nombre, "y su color es:", gato1.color)
print("El perro tiene chip?", perro1.tiene_chip())
print("El gato tiene chip?", gato1.tiene_chip())
print("El perro dice:", perro1.hablar())
print("El gato dice:", gato1.hablar())





