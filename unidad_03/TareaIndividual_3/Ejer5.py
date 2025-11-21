'''
    Autor: Manuel Fernández Jiménez
    Fecha: 17/11/2025
    Descripcion: Compara el tiempo que tarda en ejecutarse un bucle 'for'
    con el tiempo que tarda en ejecutarse la función 'sum()' para hacer lo mismo.
'''
#RA03_D
import time
#Bucle for
inicio1 = time.time()
suma1 = 0
for i in range(1, 1000001):
    suma1 += i
fin1 = time.time()
#Función sum()
inicio2 = time.time()
suma2 = sum(range(1, 1000001))
fin2 = time.time()
# Resultados
print("BUCLE FOR:")
print(f"Resultado: {suma1:,}")
print(f'Tiempo: {fin1 - inicio1:.6f} segundos\n')

print("FUNCIÓN SUM():")
print(f"Resultado: {suma2:,}")
print(f'Tiempo: {fin2 - inicio2:.6f} segundos\n')
