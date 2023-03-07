'''
Reduce
functools.reduce(funcion, iterable)
Reduce una lista a un solo elemento

Reduce hay que importarlo 
import functtools
'''
import functools
def jumpline():
  print('=' * 25)
numbers = [1,2,3,4]
# Reduce para sumar los elementos de la lista

result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)
jumpline()

# En una funcion
def accum(counter, item):
  print('Counter= ' , counter)
  print('Item =' , item)
  return counter + item

result = functools.reduce(accum, numbers)
print(result)
  