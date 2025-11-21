'''
    Autor: Manuel Fernández Jiménez
    Fecha: 17/11/2025
    Descripcion: Corrige los errores en el siguiente código
    que calcula el área de un rectángulo.
'''
#RA03_C
'''
def area_rectangulo(base, altura):
    area = base ** altura <= Hay un * de mas
    return area
base = input('Introduce la base: ') <= Falta convertir a entero
altura = input('Introduce la altura: ') <= Falta convertir a entero
area = area_rectangulo(base, altura)
print('El area es: ' area) <= Falta una coma
'''
#Correccion
def area_rectangulo(base, altura):
    area = base * altura #Corregir el operador
    return area
base = int(input('Introduce la base: ')) #Convertir a entero
altura = int(input('Introduce la altura: ')) #Convertir a entero
area = area_rectangulo(base, altura)
print('El area es: ', area) #Agregar coma