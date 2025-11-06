try:
    edad = int(input("Ingrese edad: "))
except ValueError:
    print("Error: Debe ingresar un número entero")
else:
    if edad < 18:
        print("Eres menor de edad")
    elif edad >= 18 and edad < 64:
        print("Eres adulto")
    elif edad >= 65:
        print("Eres Viejo")
