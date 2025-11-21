'''
    Autor: Manuel Fernández Jiménez
    Fecha: 14/11/2025
    Descripcion: Programa que solicita dos números enteros y un operador (+, -, * o /)
     y realiza la operación correspondiente.
'''
#RA03_B
num1 = int(input("Ingrese numero: "))
num2 = int(input("Ingrese numero: "))
operador = input("Ingrese operador (+, -, * o /): ")

if operador == "-":
    resta = num1 - num2
    print("La resta es:", resta)
elif operador == "+":
    suma = num1 + num2
    print("La suma es:", suma)
elif operador == "*":
    multipli = num1 * num2
    print("La multiplicación es:", multipli)
elif operador == "/":
    if num2 != 0:
        division = num1 / num2
        print("La división es:", division)
    else:
        print("Error: no se puede dividir entre cero")
else:
    print("Operador no valido")