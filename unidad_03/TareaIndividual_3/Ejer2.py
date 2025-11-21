'''
    Autor: Manuel Fernández Jiménez
    Fecha: 14/11/2025
    Descripcion: Muestra todos los números desde 1 hasta ese número
    utilizando tanto un bucle 'for' como un bucle 'while'.
'''
#RA03_A
num = int(input("Ingrese un numero: "))
suma = 0

print("Con for:")
for i in range(1, num + 1):
    print (i)

print("Con while:")
j = 1
while j <= num:
    print (j)
    j += 1