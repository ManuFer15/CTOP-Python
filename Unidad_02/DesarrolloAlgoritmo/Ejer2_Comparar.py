try:
    num1 = int(input("Ingresa primer numero: "))
    num2 = int(input("Ingresa segundo numero: "))
except ValueError as e:
    print("Error: No hasintroducido un valor de tipo numérico")
else:
    if num1 > num2:
        print(f"El numero {num1} es mayor que {num2}")
    elif num1 < num2:
        print(f"El numero {num2} es mayor que {num1}")
    else:
        print("Ambos numeros son iguales")
finally:
    print("Fin del programa")