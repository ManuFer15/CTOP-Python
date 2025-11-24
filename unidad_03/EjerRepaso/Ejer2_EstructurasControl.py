numero = int(input("Introduce un número del 5 al 12: "))
if numero < 5 or numero > 12:
    print("Número fuera de rango.")
else:
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

