class Saiyan:
    planeta = "Sadala"
    def __init__(self, nombre):
        self.nombre = nombre
class Goku(Saiyan):
    pass
class Vegeta(Saiyan):
    pass
personaje1 = Goku(nombre="Tierra")
personaje2 = Vegeta(nombre="Vegeta")

print(personaje1.nombre)
print(personaje2.nombre)