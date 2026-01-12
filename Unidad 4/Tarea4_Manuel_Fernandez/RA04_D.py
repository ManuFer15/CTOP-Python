##RA4_D) Se ha comprobado la eficiencia de las estructuras de datos en diferentes escenarios.
#Ejer4:  Añade al programa una tupla llamada productos_t que contenga los mismos productos que la lista productos.
print("EJERCICIO RA04_D):")
productos_t = ("manzana", "pan", "leche", "huevos", "arroz")
print(*productos_t, sep=", ")
#Explica qué diferencias hay entre usar una lista y una tupla en este caso ¿Cuándo sería mejor usar una tupla en lugar de una lista?
# Pon un ejemplo concreto.
print("\nDiferencias entre lista y tupla:")
print("\n1. Mutabilidad: Las listas son mutables, lo que significa que puedes modificar sus elementos (añadir, eliminar, cambiar)," +
      "\n mientras que las tuplas son inmutables y no pueden ser modificadas después de su creación.")
print("\n2. Uso: Las listas son ideales para colecciones de datos que pueden cambiar con el tiempo, como una lista de tareas o productos en inventario. " +
      "\nLas tuplas son más adecuadas para datos que no deben cambiar, como coordenadas geográficas o registros de datos que deben permanecer constantes.")
print("\n3. Rendimiento: Las tuplas pueden ser más eficientes en términos de rendimiento y uso de memoria debido a su inmutabilidad.")
print("\nEjemplo concreto:")
print("Si estás almacenando las coordenadas de una ubicación, es mejor usar una tupla, ya que estas coordenadas no deberían cambiar. " +
      "\nPor otro lado, si estás gestionando una lista de productos en un carrito de compras, una lista sería más adecuada, ya que los productos pueden ser añadidos o eliminados.")
