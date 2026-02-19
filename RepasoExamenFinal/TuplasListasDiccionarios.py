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
#metodos de las listas
print("Lista:", mi_lista)
print("Elemento en la posición 2:", mi_lista[1])
print("Longitud de la lista:", len(mi_lista))
mi_lista.append(6)
print("Lista después de agregar un elemento:", mi_lista)
#agrear en una posicion especifica
mi_lista.insert(3, 10)
print("Lista después de agregar un elemento en una posición específica:", mi_lista)
mi_lista.remove(3)
print("Lista después de eliminar un elemento:", mi_lista)
mi_lista[0] = 10
print("Lista después de modificar un elemento:", mi_lista)
#recorer la lista
print("Recorriendo la lista:")
for elemento in mi_lista:
    print(elemento)

##Ejemplo de diccionarios
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
#metodos de los diccionarios
print("Diccionario:", mi_diccionario)
print("Valor de la clave 'nombre':", mi_diccionario["nombre"])
print("Longitud del diccionario:", len(mi_diccionario))
mi_diccionario["profesion"] = "Ingeniero"
#agregar en una posicion especifica no es posible en los diccionarios, ya que no tienen orden
print("Diccionario después de agregar una clave-valor:", mi_diccionario)
del mi_diccionario["edad"]
print("Diccionario después de eliminar una clave-valor:", mi_diccionario)
mi_diccionario["ciudad"] = "Barcelona"
print("Diccionario después de modificar un valor:", mi_diccionario)
#recorrer el diccionario
print("Recorriendo el diccionario:")
for clave, valor in mi_diccionario.items():
    print(clave, ":", valor)
#Ejemplo de conjuntos
mi_conjunto = {1, 2, 3, 4, 5}
#metodos de los conjuntos
print("Conjunto:", mi_conjunto)
print("Longitud del conjunto:", len(mi_conjunto))
mi_conjunto.add(6)
#agregar un elemento que ya existe no genera error, simplemente no se agrega
#agregar en posicion especifica no es posible en los conjuntos, ya que no tienen orden
print("Conjunto después de agregar un elemento:", mi_conjunto)
mi_conjunto.remove(3)
print("Conjunto después de eliminar un elemento:", mi_conjunto)
#recorrer el conjunto
print("Recorriendo el conjunto:")
for elemento in mi_conjunto:
    print(elemento)
