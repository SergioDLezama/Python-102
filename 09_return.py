'''
funct Return
'''


def jumpline():
  print('=' * 25)


# Codigo que me sume todos los numeros del 1 al 1=
jumpline()
sum = 0
for x in range(1, 11):
  sum += x
print(sum)  # 55



# Mismo ejemplo pero con una funcion para poder usarlo despues
def sum(min, max):
  jumpline()
  print(min, max)
  suma = 0
  for x in range(min, max):
    suma += x
  print(suma)
  


# Puedo invocar la funcion varias veces con distintos parametros
sum(1, 500)  # 124750
sum(1, 43)  # 903
sum(33, 95)  # 3937


# Las funciones pueden retornar un valor con return
def sum(min, max):
  jumpline()
  print(min, max)
  suma = 0
  for x in range(min, max):
    suma += x
  return suma
  

  # Ahora con el return suma, en la funcion queda guardada el resultado de suma, esperando ser usado o invocado en print
print(sum(1,23)) # 253

result = sum(1,5) # 10
print(result)

result_2 = sum(result, result + 10) # 145
print(result_2)