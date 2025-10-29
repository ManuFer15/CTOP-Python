texto = ""

try:
    f = open("archivo.txt", "w")
    #texto = f.read()
    f.write("Hola, ke hase")
except Exception as e:
    print("Ocurrio un error:", e)
else:
    print("El archivo se leyo correctamente")
finally:
    f.close()