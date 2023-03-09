'''
Algunos errores y como hacer mis propios errores
'''

#print(0/0)))) # Error de Syntax

#print(0/0) # ZeroDevisionError

#print(result) # # Name error 'result' not defined

'''
Assert
'''
# La condicion de assert se cumple, no pasa nada
suma = lambda x, y: x + y
assert suma(2,2) == 4

# La condicion NO se cumple salta errpr
suma = lambda x, y: x + (y * 2)
#assert suma(2,2) == 4 # AssertionError

# Genera errores propios
age = 10
if age < 18:
  raise Exception('No se permiten menores de edad') # El programa se detiene
  