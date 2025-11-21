'''
    Autor: Manuel Fernández Jiménez
    Fecha: 14/11/2025
    Descripcion: Programa que solicita tres números enteros y muestra el mayor de ellos.
'''
#RA03_A
num1 = int(input("Ingrese numero: "))
num2 = int(input("Ingrese numero: "))
num3 = int(input("Ingrese numero: "))

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3
print("El número mayor es:", mayor)
