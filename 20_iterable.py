'''
Iterables
'''
for i in range(1,11):
  print(i)

my_iter = range(1,11)
print(my_iter) # range(1,1)

my_iter = iter(range(1,4))
print(my_iter)
print(next(my_iter)) # 1
print(next(my_iter)) # 2
print(next(my_iter)) # 3
print(next(my_iter)) # Salta error stop iteration