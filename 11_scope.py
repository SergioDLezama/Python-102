'''
El scope o alcance de variables
'''
def jumpline():
  print('>' * 25)

  # Esta variable es de alcance local, puedo usarla en cualquier momento
price = 100
print(price)
jumpline()

# Hay variables que estan solo dentro de funciones y su alcance esta limitado
def increment():
  print(price) # Puedo invocar price por que tiene alto alcance
increment()
jumpline()

# Un ejemplo de una variable local, la varible dentro de la funcion, solo existira en la funcion
def increment():
  price = 200
  price = price + 10
  print(price)
  return price

price_2 = increment()
print(price_2)
print(price) # Tiene el valor de 100 por que el valor 200 solo existe dentro de la funcion increment()
jumpline()

def increment():
  price = 200
  result = price + 10
  print(price)
  return result

# print(result) # Va dar error por que result solo esta en la funcion increment()
print(increment())