'''
Lambda Function
lambda argument : expression
'''
jumpline = '-' * 25

# Funcion sencilla que suma +1 a un valor
def increment(x):
  return x + 1
result = increment(6)
print(result)
print(jumpline)

# Puedo hacer esa funcion en una lambda
lambda x:  x + 1
increment_2 = lambda x:  x + 1
result = increment_2(9)
print(result)
print(jumpline)

# Otro ejemplo de lambda
full_name = lambda name, last_name :f'Full name is {name.title()} {last_name.title()}' 
text = full_name('sErgiO', 'LEZAMA')
print(text)
print(jumpline)