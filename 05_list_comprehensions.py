'''
List comprehensions
list = [element in element for iterable]
'''
jumpline = '='*25

numbers = []
for i in range(1,11):
  numbers.append(i)
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(jumpline)

#Todo el ciclo y la lista lo podemos hacer en una linea con list comprehension
numbers_list = [i for i in range(1,11)]
print(numbers_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(jumpline)

# Quiero que el elemento sea * 2
numbers = []
for i in range(1,11):
  numbers.append(i * 2)
print(numbers) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(jumpline)

#Tambien puedo hacerlo con list comprehension
numbers_list = [i * 2 for i in range(1,11)]
print(numbers_list) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(jumpline)

# Ejemplo con condicional de list comrprehension, quiero numeros pares del 1 al 100
numbers = [i for i in range(1,101) if i % 2 == 0]
print(numbers)
print(jumpline)

# Ejemplo sin list comprehension
numbers = []
for i in range(1,101):
  if i % 2 == 0:
    numbers.append(i)
print(numbers)
print(jumpline)