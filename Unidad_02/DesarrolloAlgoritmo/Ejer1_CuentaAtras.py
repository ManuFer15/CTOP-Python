import time as t

try:
    n = int(input("Introduce un número entre 5 y 50: "))
except ValueError as e:
    print("Error: No hasintroducido un valor de tipo numérico")
else:
    if n >= 5 and n <= 50:
        while n > 0:
            print(n)
            t.sleep(0.5)
            n -= 1
        print("¡BOOOMM!")
    else:
        print("Número fuera de rango")
finally:
    print("Fin del programa")