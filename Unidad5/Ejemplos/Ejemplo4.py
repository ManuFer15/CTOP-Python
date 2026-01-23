##Ejemplo 4
import sqlite3
conexion = sqlite3.connect('empresa.db')
cursor = conexion.cursor()
#Cear tabla empleados
cursor.execute('''CREATE TABLE IF NOT EXISTS empleados
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT,
                   salario REAL)''')
#Insertar datos
empleados = [("Carlos", 3000.0),
             ("María", 3500.5),
             ("Juan", 2800.75)]
cursor.executemany("INSERT INTO empleados (nombre, salario) VALUES (?, ?)", empleados)
conexion.commit()
#Consultar datos
cursor.execute("SELECT * FROM empleados")
filas = cursor.fetchall()
for fila in filas:
    print("ID:", fila[0], "Nombre:", fila[1], "Salario:", fila[2])
#Cerrar conexion
conexion.close()