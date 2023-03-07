'''
Como usar maps con diccionarios que son los tipos de datos mas comunes
'''
def jumpline():
  print('=' * 25)

items = [
  {
    'producto': 'camisa',
    'precio': 100
  },
  {
    'producto': 'pantalon',
    'precio': 300
  },
  {
    'producto': 'franela',
    'precio': 200
  }
]

# Usar map para pasar de lista de dicts a lista de precios (integrers)
prices = list(map(lambda item: item['precio'], items))
print(prices) # [100,300,200]
jumpline()

# Quiero que el atributo tax se sume al precio

items = [
  {
    'producto': 'camisa',
    'precio': 100,
  },
  {
    'producto': 'pantalon',
    'precio': 300
  },
  {
    'producto': 'franela',
    'precio': 200
  }
]

# Nueva lista que retorna el precio mas el 19% de tax
new_items = list(map(lambda item: item['precio'] + (item['precio'] * 0.19), items))
print(new_items)
jumpline()
# La lista items no esta modificada
print(items)
jumpline()

# anadir el key taxes al diccionario con funciones
def add_tax(item):
  item['taxes'] = item['precio'] * 0.19
  return item

new_items = list(map(add_tax, items))
print(new_items)
jumpline()

# anadir el key price_taxes con funciones
def add_tax(item):
  item['precio_taxes'] = item['precio'] + item['taxes']
  return item

new_items = list(map(add_tax, items))
print(new_items)
jumpline()

# Lista items tras la funcion, modificada
print(items)
'''
Recordar que map no modifica la list, sino crea una nueva
PERO al usar funciones si se modifica la 

Posible solucion:
copiar la lista original con .copy() y modificar la copia
'''
