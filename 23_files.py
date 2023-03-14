'''
Como leer un archivo de texto plano .txt
con open()
'''
def jumpline():
  print('=' * 30)

# Abro el archivo con open()
file = open('./text.txt')

# Leer un archivo completo
print(file.read())
jumpline()

# Leer una linea
file = open('./text.txt')
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

# .read() Consume mucha memoria, es importante usar close()
file.close()
jumpline()

'''
El read es muy peado y poco practivo para archivos grandes
El readline es mas ligero pero no siempre sabemos cuantas lineas tiene el archivo
Usamos un for para eso
'''

file = open('./text.txt')
for line in file:
  print(line)
jumpline()

file.close()

# Para que python cierre automaticamente un archivo:

print('Otro metodo')

with open('./text.txt') as file:
  for line in file:
    print(line)
