import random
jumpline = '=' * 25

countries = ['col', 'mex', 'bol', 'pe']
population_2 = {i: random.randint(1,100) for i in countries}
print(population_2)
print(jumpline)

# Quiero generar otro diccionario donde solo me devuelva los paises mayores de 20
result = {country : population for (country, population) in population_2.items() if population > 20}
print(result)
print(jumpline)

# Otro ejemplo
text = 'Hola soy sergio'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)
print(jumpline)

text = 'Hola soy sergio quiero ver cuantas veces aparece una vocal en este string'
unique = { c: text.count(c) for c in text if c in 'aeiou' }
print(unique)