"""-----Apartado 1-----"""
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

def info_libro(libro):
    return f"Título: {libro._Libro__titulo}, Autor: {libro._Libro__autor}"

lb1= Libro("Don Quijote", "Miguel de Cervantes", "1234567890")
lb2= Libro("Cien Años de Soledad", "Gabriel García Márquez", "0987654321")

print("Apartado 1:")
print(info_libro(lb1))
print(info_libro(lb2))

"""-----Apartado 2-----"""
class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, tamanioMb):
        super().__init__(titulo, autor, isbn)
        self._tamanioMb = tamanioMb

def info_digital(self):
    return f"{info_libro(self)}, Tamaño: {self._tamanioMb} MB"

LibroDigital.info_digital = info_digital
ld1 = LibroDigital("1984", "George Orwell", "1122334455", 2)
ld2 = LibroDigital("El Principito", "Antoine de Saint-Exupéry", "5544332211", 1.5)
print("\nApartado 2:")
print(ld1.info_digital())
print(ld2.info_digital())

"""-----Apartado 3-----"""
import sqlite3
conexion = sqlite3.connect('biblioteca.db')
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS libros
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT,
                   autor TEXT,
                   isbn TEXT)''')

libros = [(lb1._Libro__titulo, lb1._Libro__autor, lb1._Libro__isbn),
          (lb2._Libro__titulo, lb2._Libro__autor, lb2._Libro__isbn),
          (ld1._Libro__titulo, ld1._Libro__autor, ld1._Libro__isbn),
          (ld2._Libro__titulo, ld2._Libro__autor, ld2._Libro__isbn)]

def insertar_libros(lista_libros):
    cursor.executemany("INSERT INTO libros (titulo, autor, isbn) VALUES (?, ?, ?)", lista_libros)
    conexion.commit()
def mostrar_libros():
    cursor.execute("SELECT * FROM libros")
    filas = cursor.fetchall()
    for fila in filas:
        print("ID:", fila[0], "Título:", fila[1], "Autor:", fila[2], "ISBN:", fila[3])

insertar_libros(libros)
print("\nApartado 3:")
mostrar_libros()

cursor.close()
conexion.close()