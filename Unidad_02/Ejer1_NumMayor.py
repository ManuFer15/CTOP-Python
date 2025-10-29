num1 = int(input("Introduce primer número: "))
num2 = int(input("Introduce segundo número: "))
if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print("Ambos números son iguales.")