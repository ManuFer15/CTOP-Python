##RA05_A:
#Ejer1:
class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
def info_producto(producto):
    return f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio} €"

prod1 = Producto(1, "Portatil", 1200.50)
prod2 = Producto(2, "Movil", 800.75)

print("RA05_A: Ejer1")
print(info_producto(prod1))
print(info_producto(prod2))

##RA05_B:
#Ejer2:
class ProductoPrivado:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def set_precio(self, newPrecio):
        if newPrecio >= 0:
            self.__precio = newPrecio
        else:
            print("El precio no puede ser negativo.")

def info_producto_privado(producto):
    return f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.get_precio()} €"

prod3 = ProductoPrivado(3, "Tablet", 450.00)
prod4 = ProductoPrivado(4, "Play Station", 500.00)

print("\nRA05_B: Ejer2")
print(info_producto_privado(prod3))
print(info_producto_privado(prod4))

##RA05_C:
#Ejer3:
