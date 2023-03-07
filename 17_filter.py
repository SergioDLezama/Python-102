'''
Filter
filter(function, iterable)

Filter no modifica la lista original
'''
# Filtrando los numeros pares
numbers = [1,2,3,4,5]
new_numbers = filter(lambda x : x % 2 == 0, numbers)

print(new_numbers)
print(numbers)
print(list(new_numbers))
