def suma(a, b):
    suma = a + b
    print("Suma: ", suma)

def resta(a, b):
    resta = a - b
    print("Resta: ", resta)

def multiplicacion(a, b):
    multi = a * b
    print("Multiplicacion: ", multi)

def division(a, b):
    if b == 0:
        return "Nose puede dividir entre cero"
    division = a / b
    print("Division: ", division)


if __name__ == '__main__':
    print("Este modulo tiene operaciones basicas")