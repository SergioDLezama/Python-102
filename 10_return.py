'''
Multiples return
'''
def jumpline():
  print('-' * 25)

# Funcion para encontrar el volumen
def find_volume(length, width, depth):
  return length * width * depth

# Si intento ejecutar la funcion sin asignarle parametros nme va dar error
#result = find_volume()
#print(result) # TypeError

result = find_volume(10, 20, 3)
print(result) # 600
jumpline()

# Puedo asignar un valor por defecto en caso que no me den cierto argumento
def find_volume(length = 3, width = 15, depth = 2):
  return length * width * depth

result = find_volume()
print(result) # 90 Resultado de la multiplicacion de los valores por defecto
jumpline()

# Quiero solo asignar un valor, por ejemplo width
def find_volume(length = 3, width = 15, depth = 2):
  return length * width * depth

result = find_volume(width = 10)
print(result) # 60
jumpline()

# Tambien puedo retornar mas de una funcion
def find_volume(length = 3, width = 15, depth = 2):
  return length * width * depth, 'Volume', width

result = find_volume(width = 30)
print(result) # (180, 'Volume: ', 30) Me devuelve una tupla

print(result[0]) # 180
jumpline()

# Puedo de una vez asignar una variable a cada elemento de la tupla
result, text, width = find_volume(width = 30)
print(result, text, width) # 180 Volume 30
print(result) # 180
print(text) # Volume
print(width) # 30