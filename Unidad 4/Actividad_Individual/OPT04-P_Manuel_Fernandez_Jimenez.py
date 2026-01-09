##Ejerer1:
print("EJERCICIO 1:")
Estudiantes = ["Manu", "Ana", "Luis", "Marta", "Sofia"]
print(Estudiantes)
#Añado uno mas
nuevo_estudiante = input("Introduce el nombre del nuevo estudiante: ")
Estudiantes = Estudiantes + [nuevo_estudiante,]
print("Lista después de añadir un estudiante:")
print(Estudiantes)
#Elimino uno concreto
estudiante_eliminar = input("Introduce el nombre del estudiante a eliminar: ")
if estudiante_eliminar in Estudiantes:
    Estudiantes.remove(estudiante_eliminar)
    print("Lista después de eliminar un estudiante:")
    print(Estudiantes)
else:
    print(f"El estudiante {estudiante_eliminar} no está en la lista.")
#Ordeno la lista
Estudiantes.sort()
print("Lista ordenada de estudiantes:")
print(Estudiantes)

##Ejerer2:
print("\nEJERCICIO 2:")
Calificaciones = {"Manu": 8, "Ana": 9, "Luis": 7, "Marta": 9, "Sofia": 4}
print(Calificaciones)
#Añado una nueva calificación o actualizo
nuevo_nombre = input("Introduce el nombre del estudiante para añadir/actualizar calificación: ")
nueva_calificacion = int(input(f"Introduce la calificación de {nuevo_nombre}: "))
Calificaciones[nuevo_nombre] = nueva_calificacion
print("Diccionario después de añadir/actualizar calificación:")
print(Calificaciones)
#Consulto una calificación con get()
nombre_consulta = input("Introduce el nombre del estudiante para consultar su calificación: ")
calificacion = Calificaciones.get(nombre_consulta, "Estudiante no encontrado")
print(f"La calificación de {nombre_consulta} es: {calificacion}")
#Muestro todas las calificaciones
print("Todas las calificaciones:")
for nombre, calificacion in Calificaciones.items():
    print(f"{nombre}: {calificacion}")
#Calculo la media
media = sum(Calificaciones.values()) / len(Calificaciones)
print(f"La calificación media es: {media:.2f}")

##Ejerer3:
print("\nEJERCICIO 3:")
with open("alumnos.txt", "w") as archivo:
    for nombre, calificacion in Calificaciones.items():
        archivo.write(f"{nombre} - {calificacion}\n")
print("Información guardada en alumnos.txt")