palabras = []
contador = 0
print("¡Comienza el juego! Escribe palabras o 'Basta' para terminar.")
try:
    while True:
        palabra = input("Introduce una palabra: ")

        if palabra == "" or palabra.lower() == "basta":
            break
        palabras.append(palabra)
        contador += 1
        print(" ".join(palabras))
    print(f"Has soportado estoicamente {contador} preguntas")
except Exception as e:
    print("Ha ocurrido un error:", e)
finally:
    print("Fin del programa")

