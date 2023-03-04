'''
Map
Funcion interna de Python que transforma elementos

map(funcion, iterables)
'''

# Si quisiera modificar esta lista usaria un ciclo y una nueva lista
numbers = [1, 2, 3, 4]
numbers_v2 = []

for i in numbers:
  numbers_v2.append(i * 2)

print(numbers)
print(numbers_v2)

# Podemos hacer esto con map y lambda 
numbers_v3 = list(map(lambda i: i * 2, numbers))
print(numbers_v3)

# Otro atributo de map()
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))

print(numbers_1)
print(numbers_2)
print(result) # Devolveria 3 items por que la lista mas pequena tenia 3