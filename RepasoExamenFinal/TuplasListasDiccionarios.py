##Ejemplo de tuplas
mi_tupla = (1, 2, 3, 4, 5)
print("Tupla:", mi_tupla)
print("Elemento en la posición 2:", mi_tupla[1])
print("Longitud de la tupla:", len(mi_tupla))
# Las tuplas son inmutables, por lo que no se pueden modificar ni agregar elementos
#recorrer la tupla
print("Recorriendo la tupla:")
for elemento in mi_tupla:
    print(elemento)
##Ejemplo de listas
mi_lista = [1, 2, 3, 4, 5]
print("Lista:", mi_lista)
print("Elemento en la posición 2:", mi_lista[1])
print("Longitud de la lista:", len(mi_lista))
mi_lista.append(6)
print("Lista después de agregar un elemento:", mi_lista)
mi_lista[0] = 0
print("Lista después de modificar el primer elemento:", mi_lista)
#recorer la lista
print("Recorriendo la lista:")
for elemento in mi_lista:
    print(elemento)

##Ejemplo de diccionarios
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print("Diccionario:", mi_diccionario)
print("Valor de la clave 'nombre':", mi_diccionario["nombre"])
print("Valor de la clave 'edad':", mi_diccionario["edad"])
print("Valor de la clave 'ciudad':", mi_diccionario["ciudad"])
print("Claves del diccionario:", mi_diccionario.keys())
print("Valores del diccionario:", mi_diccionario.values())
print("Elementos del diccionario:", mi_diccionario.items())
mi_diccionario["profesion"] = "Ingeniero"
print("Diccionario después de agregar una nueva clave-valor:", mi_diccionario)
#recorrer el diccionario
print("Recorriendo el diccionario:")
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")

