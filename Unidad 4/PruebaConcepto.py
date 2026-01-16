##1. Escribe un programa que use una tupla con 5 valores numéricos: 5, 1, 4, 3 y 2
numeros = (5, 1, 4, 3, 2)
#Recorre la tupla y almacena los valores de la tupla elevados al cubo (3) en una lista.
cubos = []
for numero in numeros:
    cubos.append(numero ** 3)
#Ordena la lista y muestra el contenido de la tupla y de la lista en pantalla
cubos.sort()
print("Tupla original:", numeros)
print("Lista de cubos ordenada:", cubos)

##2. Escribe un programa que itere y muestre en pantalla el contenido de un diccionario cuyas claves sean: nombre, apellidos y notas de 4 estudiantes.
estudiantes = {
    "estudiante1": {"nombre": "Ana", "apellidos": "García", "notas": [8, 9, 7]},
    "estudiante2": {"nombre": "Luis", "apellidos": "Martínez", "notas": [6, 7, 8]},
    "estudiante3": {"nombre": "Marta", "apellidos": "López", "notas": [9, 10, 9]},
    "estudiante4": {"nombre": "Carlos", "apellidos": "Sánchez", "notas": [5, 6, 7]},
}
for clave, info in estudiantes.items():
    print(f"{clave}: Nombre: {info['nombre']}, Apellidos: {info['apellidos']}, Notas: {info['notas']}")

##3. Escribe un programa que cree un archivo llamado "prueba1.txt” y grabe en él el texto: “El conceto es el conceto...”.
with open("prueba1.txt", "w") as archivo:
    archivo.write("El conceto es el conceto...")
#Luego, debe abrir el archivo anterior y añadir el texto: “Pazos (Airbag)”.
with open("prueba1.txt", "a") as archivo:
    archivo.write(" Pazos (Airbag)")
#Finalmente, debes cerrar el archivo.
# (El uso de 'with' se encarga de cerrar el archivo automáticamente)

##4.  Escribe un programa que contenga una lista con los siguientes datos de un alumno: nombre, edad, teléfono.
alumno = ["Manu", 21, "123456789"]
#Después, modifica la edad y elimina el teléfono.
alumno[1] = 22
alumno.pop(2)
#Luego, añade a la lista anterior a su vez otra lista con 3 notas del alumno, y para terminar, muéstrala en pantalla
notas = [8.5, 9.0, 7.5]
alumno.append(notas)
print("\nDatos del alumno:")
print("Nombre:", alumno[0])
print("Edad:", alumno[1])
print("Notas:", alumno[2])


