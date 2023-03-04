'''
Funciones

def namefunct():
  code

funcion(argumento)
'''
# Funcion parahacer una linea de = para dividir en la consola 
def jumpline():
  print('='*25)
# print() es una funcion y de argumento tiene 'hola'
print('Hola')

# Defino mi funcion de prueba
def my_print():
  print('This is my print')
  print('This is a second print()')
my_print()
jumpline()

# Puedo darle parametros a mis funciones
def my_print(text):
  print(text * 2)
my_print('This is my text')
jumpline()

# Cuando le doy un parametro le asigno un lugar a mi codigo para que me lo devuelvan como un armgumento
my_print('Hola este es mi texto ')
jumpline()

# Normalmente para hacer una suma con dos variables tendriamos que escribir todo asi
a = 10
b = 90
c = a + b

# Pero si tengo que usar una suma varias veces uso las funciones
def suma(a, b):
  print(a + b)
  jumpline()
suma(90, 10) # 100 
suma(30, 71) # 101
suma(33, 753) # 786

# Tambien una funcion puede tener otra
def suma(a, b):
  my_print(a + b)
  jumpline()
suma(90, 10) # 200
suma(30, 71) # 202
suma(33, 753) # 1572