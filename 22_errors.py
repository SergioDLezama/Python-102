'''
Manejo de errores
'''
'''
print(0/0)

# Naturalmente esto no se va ejecutar por el error de 0/0
print('Prueba 01!')
'''

# Ponemos como excepcion el ZeroDivisionError
try:
  print(0/0)
except ZeroDivisionError as error:
  print('Tuvimos un problema ', error)
# Ahora si se ejecuta el print
print('Prueba 01')

'''
# Otro ejemplo
assert 1 != 1, 'Uno no es igual a uno'

# Tampoco se ejecuta por el error arriba, tenemos que poner el assert en un try
print('Prueba 2')
'''
# Solucion
try:
  assert 1 != 1, 'Uno no es igual a uno'
except AssertionError as aserror:
  print(aserror)

# Ahora si corrio la prueba
print('Prueba 02!')

'''
# Otro ejemplo

age = 10
if age < 18:
  raise Exception('No se permiten menores de edad')

#No se ejecuta por el error de excepcion
print('Prueba 03!')
'''

# Solucion al except
age = 10
try:
  if age < 18:
    raise Exception('No se permiten menores de edad')
except Exception as error:
  print(error)

# Ahora si se ejecuta
print('Prueba 03!')

print('=' * 30)

'''
Todos los except pueden ir en un solo try

Solo va ejecutar el primer error en este caso el exception
NO va a saltar cada error pero si va correr el print de prueba
'''
try:
  print(0/0)
  assert 1 != 1, 'Uno no es igual a uno'
  if age < 18:
    raise Exception('No se permiten menores de edad')
except Exception as error:
  print('Error 01' ,error)
except ZeroDivisionError as error:
  print('Error 02 ', error)
except AssertionError as aserror:
  print('Error 03 ' ,aserror)

print('PRUEBA TOTAL')