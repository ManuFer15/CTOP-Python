try:
    num = int(input("Ingresa un numero: "))
    print("El numero ingresado es:", num)
except ValueError as e:
    print("Error: Debes ingresar un numero valido.")
else:
    print("El numero se ingreso correctamente.")
finally:
    print("Fin del programa.")