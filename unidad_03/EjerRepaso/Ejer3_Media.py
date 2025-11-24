#Apartado 1: Media de dos numeros
def calrcularMedia():
    try:
        num1 = int(input("Ingresa un numero: "))
        num2 = int(input("Ingresa otro numero: "))
    except ValueError:
        print("Error: Debes ingresar numeros enteros.")
    else:
        media = (num1 + num2) / 2
        return media

#Apartado 2: Media de varios numeros
def mediaVariabeles(*numeros):
    if len(numeros) == 0:
        return 0
    suma = sum(numeros)
    media = suma / len(numeros)
    return media

print("Media de dos numeros:", calrcularMedia())
print("\nMedia de varios numeros:", mediaVariabeles(13, 2, 64, 9))
