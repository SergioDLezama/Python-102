'''
Dictionaty Comprehensions

{key: value for var in iterable}
'''
jumpline = '=' * 25

# Voy a crear una lista donde el key sea un numero y el valor sea el numero * 2
dict = {}
for i in range(1,5):
  dict[i] = i * 2
print(dict) # {1: 2, 2: 4, 3: 6, 4: 8}
print(jumpline)

# Puedo crear la misma lista con comprehensions
dict_v2 = {i : i*2 for i in range(1,5)}
print(dict_v2) # {1: 2, 2: 4, 3: 6, 4: 8}
print(jumpline)

# Generemos un diccionario a partir de una lista donde el key sea el nombre del pais y value una poblacion aleatoria entre 1 y 150
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for i in countries:
  population[i] = random.randint(1, 150)
print(population)
print(jumpline)

# Tambien podemos hacerlo con list comprehension
countries = ['col', 'mex', 'bol', 'pe']
population_2 = {i: random.randint(1,150) for i in countries}
print(population_2)
print(jumpline)

# Ahora generaremos un diccionario a partir de dos listas
names = ['sergio', 'mathias', 'maxi']
ages = [20, 11, 9]
# Puedo unir las listas con .zip(lista,lista) y se vuelve una lista de tuplas
brothers = {name: age for (name, age) in zip(names, ages)}
print(brothers)

# Otra forma de hacer este ejercicio
brothers_2 = {names[i]: ages[i] for i in range(len(names))}
print(brothers_2)
