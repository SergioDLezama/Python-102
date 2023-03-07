'''
Vamos a resolver el reto del curso anterior, donde la idea 
era modificar el atributo de in dict sin modificar la lista original
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

# Solucion .copy() Esta funcion hace una copia de la lista
def add_tax(item):
  new_item = item.copy()
  new_item['taxes'] = new_item['precio'] * 0.19
  return new_item

new_items = list(map(add_tax, items))
print('New List')
print(new_items)
print('Old list')
print(items)