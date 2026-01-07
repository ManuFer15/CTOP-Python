##Ejer1: Añade un número al final Elimina el último número Muestra solo los 3 primeros elementos
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
numeros.remove(6)
print(numeros[:3])

##Ejer2: Dada una lista de nombres, comprueba si "Ana" está en la lista.
nombres = ["Luis", "Ana", "Pedro", "Marta"]
if "Ana" in nombres:
    print("Ana esta")

##Ejer3: Crea una tupla con 4 colores y accede al segundo color Comprueba si "rojo" está en la tupla
colores = ("azul", "verde", "rojo", "amarillo")
print(colores[1])
if "rojo" in colores:
    print("Rojo esta")

##Ejer4: Intenta modificar un elemento de la tupla. 👉 Observa el error y entiende por qué ocurre.
colores = ("azul", "verde", "rojo", "amarillo")
#colores[1] = "naranja"  # Esto generará un error porque las tuplas son inmutables

#Ejer5: Crea un array de enteros y cambia el valor del primer elemento Intenta asignar un valor de tipo incorrecto
from array import array
nums = array('i', [1, 2, 3, 4, 5])
nums[0] = 10
#print(nums)
#nums[1] = "veinte"  # Esto generará un error porque el tipo es incorrecto

#Ejer6: Crea un diccionario con información de una persona. Luego, añade la clave "ciudad" Elimina la clave "edad"
persona = {"nombre": "Juan", "edad": 30}
persona["ciudad"] = "Madrid"
del persona["edad"]
print(persona)

#Ejer7: Recorre el diccionario anterior e imprime las claves y valores.
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

#Ejer8: Simula una pila usando una lista. Añade 3 números Elimina el último Muestra la pila final
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
pila.pop()
print(pila)

#Ejer9: Simula una cola usando deque. Añade 3 elementos Elimina el primero Muestra la cola resultante
from collections import deque
cola = deque()
cola.append(1)
cola.append(2)
cola.append(3)
cola.popleft()
print(cola)
#Ejer10: Dada una lista de números: Ordénala Obtén el valor máximo Obtén el valor mínimo
nums = [4,7,1,9,2]
nums.sort()
print(f"Ordenada: {nums}")
print(f"Maximo: {max(nums)}")
print(f"Minimo: {min(nums)}")