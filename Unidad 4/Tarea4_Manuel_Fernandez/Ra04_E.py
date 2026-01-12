##RA4_E) Se han integrado estructuras de datos avanzadas para resolver problemas más complejos de almacenamiento y acceso a la información.
#Ejer5: Crea un diccionario anidado llamado almacen donde cada producto tenga asociada más información, como:
print("EJERCICIO RA04_E):")
almacen = {
    "manzana": {"precio": 0.5, "cantidad": 50},
    "pan": {"precio": 1.0, "cantidad": 30},
    "leche": {"precio": 0.8, "cantidad": 20},
    "huevos": {"precio": 0.2, "cantidad": 100},
    "arroz": {"precio": 1.5, "cantidad": 80}
}
# Muestra el precio de un producto concreto.
nombreConsulta = input("Introduce el nombre del producto para consultar: ")
if nombreConsulta in almacen:
    precio = almacen[nombreConsulta]["precio"]
    print(f"El precio de {nombreConsulta} es: {precio}€")
else:
    print(f"El producto {nombreConsulta} no está en el almacén.")
#Muestra todos los productos con stock inferior a un valor dado.
valorStock = int(input("\nIntroduce un valor de stock para filtrar productos: "))
print(f"Productos con stock inferior a {valorStock}:")
for producto, info in almacen.items():
    if info["cantidad"] < valorStock:
        print(f"{producto}: {info['cantidad']} unidades")
#Calcula el valor total del stock (precio × cantidad).
valorTotal = sum(info["precio"] * info["cantidad"] for info in almacen.values())
print(f"\nValor total del stock: {valorTotal}€")


