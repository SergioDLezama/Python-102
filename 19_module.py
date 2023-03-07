'''
Modulos
'''
def jumpline():
  print('-' * 30)
import sys

# Para saber en que ubicacion esta el archivo que estoy ejecutando
print(sys.path)
jumpline()

# Modulo de Expresiones regulares
import re
text = 'Mi numero de telefono es 412 7547785, el codigo de pais es +58, numero de suerte 3'
# Buscar strings con numeros con Expresiones regulares
result = re.findall('[0-9]+', text)
print(result) # ['412', '7547785', '58', '3']
jumpline()

# Manejo de horas y fechas
import time
timestamp = time.time()
print(timestamp)
# Formato local de hora en la maquina no siempre es el horario local
local = time.localtime()
result = time.asctime(local)
print(result)
jumpline()

# Collections
import collections
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter) # Counter({1: 4, 2: 2, 3: 2, 4: 1, 5: 1, 21: 1})