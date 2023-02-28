'''
Conjuntos

Conjutos agrupan elementos que tienen algo en comun

setname = {item, item, item}
'''
jumpline = '-' * 25
set_countries = {'col', 'mex', 'bol'}

print(set_countries) # {'col', 'mex', 'bol'}
print(type(set_countries)) # <class 'set'>
print(jumpline)

#No puedo tener items repetidos, al hacer print los va eliminar
set_countries = {'col', 'mex', 'bol', 'col'} 
print(set_countries) # {'col', 'mex', 'bol'}
print(jumpline)

set_numbers = { 1, 2, 2, 443, 23}
print(set_numbers) # {1, 2, 443, 23}
print(jumpline)

# Tambien puedo almacenar diferentes tipos de datos
# No importa el orden que le demos
set_types = {1, 'Hola', False, 12.2}
print(set_types) # {False, 1, 12.2, 'Hola'}
print(jumpline)

# Puedo crear un set a partir de un string
set_from_string = set('hola')
print(set_from_string) # {'l', 'a', 'h', 'o'}
print(jumpline)

set_from_string = set('hoooolaaaaa')
print(set_from_string) # {'l', 'a', 'h', 'o'}
print(jumpline) 

# Puedo crear un set a partir de una tupla
set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples) # {'as', 'cbv', 'abc'}
print(jumpline)

# Puedo igualmente hacer sets desde una lista
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers) # {1,2,3,4}
unique_numbers = list(set_numbers)
print(unique_numbers) # {1,2,3,4}
print(unique_numbers[1]) # 2
print(jumpline)
