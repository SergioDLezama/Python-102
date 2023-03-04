'''
Higer Order Functions
'''
jumpline = '\n' + '-' * 25


def increment(x):
  return x + 1

def ex_hof(x, func):
  return x + func(x)

result = ex_hof(2 , increment) # 2 + (x + 1)
print(result, jumpline) # 5

# Podemos aplicar una lambda para mejorar la estructura
def increment(x):
  return x + 1

increment_lambd = lambda x : x + 1

def ex_hof(x, func):
  return x + func(x)

ex_hof_lambd = lambda x, func : x + func(x)

result = ex_hof_lambd(2 , increment) # 2 + (x + 1)
print(result,jumpline) # 5
result = ex_hof_lambd(2 , lambda x : x + 1) # 2 + (x + 1)
print(result,jumpline) # 5

result = ex_hof_lambd(3 , lambda x : x * 8) # 3 + (x * 8)
print(result, jumpline) # 27