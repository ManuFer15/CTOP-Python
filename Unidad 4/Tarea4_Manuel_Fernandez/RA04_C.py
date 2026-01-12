##RA4_C) Se han implementado estructuras de datos en programas para almacenar y procesar información.
#Ejer3:  Crea un diccionario llamado stock donde:
print("EJERCICIO RA4_C):")
stock ={"manzana": 50, "pan": 30, "leche": 20, "huevos": 100, "arroz": 80}
#Una vez hecho esto, define 2 funciones: una que calcule el número total de productos disponibles (suma de todos los valores)
# y otra que muestre todos los productos cuyo stock supere una cantidad dada (p.ej. mayor que 10).
def totalProduc(stockProduc):
    return sum(stockProduc.values())

def producMayor(stockProduc, cantidadDada):
    return {producto: cantidad for producto, cantidad in stockProduc.items() if cantidad > cantidadDada}

total = totalProduc(stock)
print(f"Número total de productos disponibles: {total}")
cantidadQuerida = int(input("\nIntroduce una cantidad para filtrar productos: "))
producFiltrer = producMayor(stock, cantidadQuerida)
print(f"Productos con stock mayor que {cantidadQuerida}:")
for producto, cantidad in producFiltrer.items():
    print(f"{producto}: {cantidad}")


