import sys
lista = [1, 2, 3, 4]

try:
    for n in lista:
        print(n)
except IndexError as e:
    print("Error: ", e)
else:
    print("Finalizo correctamente")
finally:
    sys.exit(0)
