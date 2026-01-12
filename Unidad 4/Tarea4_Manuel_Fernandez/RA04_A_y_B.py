##RA04_A) Se han declarado y manipulado listas, tuplas y diccionarios
#Ejer1: Crea una lista llamada productos que contenga al menos 5 nombres de productos que conozcas.
print("EJERCICIO RA04_A):")
productos = ["manzana", "pan", "leche", "huevos", "arroz"]
print("Lista inicial de productos:")
print(*productos, sep=", ")
#Muestra el primer y el último elemento de la lista.
print("\nPrimer producto:", productos[0])
print("Último producto:", productos[-1])
#Añade un nuevo producto a la lista usando el metodo append()
newProducto = input("\nIntroduce el nombre de un nuevo producto para añadir: ")
productos.append(newProducto)
print("Lista actualizada:")
print(*productos, sep=", ")

##RA4_B) Se han aplicado métodos y funciones integradas para el manejo de estructuras de datos.
#Ejer2: A partir de la lista productos creada anteriormente:
print("\nEJERCICIO RA4_B):")
#Ordena la lista en orden alfabético y muestra en pantalla
productos.sort()
print("Lista ordenada alfabéticamente:")
print(*productos, sep=", ")
#Elimina un producto concreto y muestrala en pantalla
producBorrado = input("\nIntroduce el nombre del producto a eliminar: ")
if producBorrado in productos:
    productos.remove(producBorrado)
    print("Lista actualizadad:")
    print(*productos, sep=", ")
else:
    print(f"El producto {producBorrado} no está en la lista.")
