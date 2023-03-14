'''
Como escribir un archivo
'''

def jumpline():
  print("=" * 25)

# Con este codigo unicamente puedo leer el archivo
with open('./text.txt') as file:
  for line in file:
    print(line)
jumpline()
# Para tener permiso de escritura 'w'
#with open('./text.txt', 'w') as file:

# Para que tenga permisos de escribir y leer 'r+'
with open('./text.txt', 'r+') as file:
  for line in file:
    print(line)
  file.write('\nTengo permisos')  # El archivo se modifica anadiendo esa linea al final
# Por cada vez que lo ejecute se vuelve a escribir

# Para SOBREESCRIBIR
with open('./text.txt', 'w+') as file:
  for line in file:
    print(line)
  file.write('\nTengo permisos')  # El archivo se sobreescribe
