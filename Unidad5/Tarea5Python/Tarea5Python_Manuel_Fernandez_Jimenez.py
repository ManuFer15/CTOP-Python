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
class ProductoPrivado(Producto):
    def __init__(self, id, nombre, precio):
        super().__init__(id, nombre, precio)
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
class ProductoAlimenticio(Producto):
    def __init__(self, id, nombre, precio, fechaCaducidad):
        super().__init__(id, nombre, precio)
        self.fechaCaducidad = fechaCaducidad

    def comprobarCaducidad(self, fechaActual):
        if fechaActual < self.fechaCaducidad:
            return "No caducado"
        else:
            return "Caducado"
pAli1 = ProductoAlimenticio(5, "Leche", 1.20, "2024-12-01")
pAli2 = ProductoAlimenticio(6, "Yogur", 0.80, "2024-05-15")
print("\nRA05_C: Ejer3")
print(f"Producto: {pAli1.nombre}, Estado: {pAli1.comprobarCaducidad('2026-06-01')}")
print(f"Producto: {pAli2.nombre}, Estado: {pAli2.comprobarCaducidad('2026-06-01')}")


##RA05_D:
#Ejer4:
#import sqlite3

#conn = sqlite3.connect('productos.db')
#cursor = conn.cursor()
#cursor.execute('''CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL, fechaCaducidad TEXT)''')

##RA05_E:
#Ejer5:
#cursor.execute("INSERT INTO productos (id, nombre, precio, fechaCaducidad) VALUES (?, ?, ?, ?)", (id, "pan", "0.50", "2026-06-10"))
#conn.commit()
#cursor.execute("SELECT * FROM productos")
#cursor.fetchall()
#cursor.close()
#conn.close()

##RA05_F:
#Ejer6:
import sqlite3
class GestorBD:
    def __init__(self, db_name='productos.db'):
        self.conn = sqlite3.connect(db_name)

        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL, fechaCaducidad TEXT)''')

    def agregar_producto(self, producto):
        self.cursor.execute("INSERT INTO productos (id, nombre, precio, fechaCaducidad) VALUES (?, ?, ?, ?)",
                            (producto.id, producto.nombre, producto.precio, getattr(producto, 'fechaCaducidad', None)))
        self.conn.commit()

    def obtener_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()

    def cerrar(self):
        self.cursor.close()
        self.conn.close()

gestor = GestorBD()
gestor.agregar_producto(pAli1)
gestor.agregar_producto(pAli2)
productos = gestor.obtener_productos()
print("\nRA05_F: Ejer6")
for prod in productos:
    print(prod)
gestor.cerrar()
