##Ejemplo 1
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
#Crear objeto
u = Usuario("Ana", 22)
#Gruadar el objeto en una base de datos SQLite
import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, edad INTEGER)')
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (u.nombre, u.edad))

conexion.commit()
print("Usuario guardado en la base de datos.")
conexion.close()