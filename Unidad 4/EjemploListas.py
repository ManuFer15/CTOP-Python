nums = [1, 2, 3, 4,]
## añair al final de la lista
nums.append(5)
print("Lista después de añadir 5 al final:")
print(nums)
## añadir en una posición específica
nums.insert(0, 0)
print("Lista después de añadir 0 al inicio:")
print(nums)
## eliminar un elemento por valor
nums.remove(3)
print("Lista después de eliminar el valor 3:")
print(nums)
## eliminar un elemento por índice
del nums[2]
print("Lista después de eliminar el elemento en el índice 2:")
print(nums)
## obtener el índice de un elemento
index_of_4 = nums.index(4)
print(f"El índice de 4 es: {index_of_4}")
## contar cuántas veces aparece un elemento
count_of_2 = nums.count(2)
print(f"El número 2 aparece {count_of_2} veces")
## ordenar la lista
nums.sort()
print(f"Lista ordenada: {nums}")
## invertir la lista
nums.reverse()
print(f"Lista invertida: {nums}")
## obtener la longitud de la lista
length = len(nums)
print(f"La longitud de la lista es: {length}")
## recorrer la lista
print("Elementos de la lista:")
for num in nums:
    print(num)
## limpiar la lista
nums.clear()
print(f"Lista después de limpiar: {nums}")