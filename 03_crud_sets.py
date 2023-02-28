jumpline = '-' * 25
set_countries = {'col', 'mex', 'bol'}

# Con len() puedo saber la longitud de el set
size = len(set_countries)
print(size) # 3
print(jumpline)

# Verificar si un elemento esta dentro de este conjunto
print('col' in set_countries) # True
print('pe' in set_countries) # False
print(jumpline)

# Adicionar elementos al set con .add()
print(set_countries) # {'col', 'mex', 'bol'}
set_countries.add('pe')
print(set_countries) # {'col', 'pe', 'mex', 'bol'}

# Aunque le pida adicionar otro elemento si esta repetido no lo agrega
set_countries.add('pe')
print(set_countries) # {'col', 'pe', 'mex', 'bol'}
print(jumpline)

# .update() Para actualizar un conjunto usar {} 
print(set_countries) # {'col', 'pe', 'mex', 'bol'}
set_countries.update({'ar', 'ecua', 'pe'})
print(set_countries) # {'col', 'pe', 'mex', 'ar', 'ecua', 'bol'}
print(jumpline)

# Remover elementos tiene diferentes metodos
print(set_countries) # {'col', 'pe', 'mex', 'ar', 'ecua', 'bol'}
set_countries.remove('col')
print(set_countries) # {'pe', 'mex', 'ar', 'ecua', 'bol'}
set_countries.remove('ar')
print(set_countries) # {'pe', 'mex', 'ecua', 'bol'}
print(jumpline)

# Si no estamos seguros que un elemento esta para borrarlo .remove() dara error
#set_countries.remove('arg') # Syntax error
# Usamoos .discard() cuando no estamos seguros. Si el elemento no existe no saltara el error
set_countries.discard('arg') # No pasa nada
print(jumpline)

# Corrigo el error de argentina abreviado
print(set_countries) # {'pe', 'mex', 'ecua', 'bol'}
set_countries.add('arg')
print(set_countries) # {'pe', 'mex', 'arg', 'ecua', 'bol'}
print(jumpline)

# Puedo limpiar completamente un set con .clear()
print(set_countries) # {'pe', 'mex', 'arg', 'ecua', 'bol'}
set_countries.clear()
print(set_countries) # set()
print(len(set_countries)) # 0
print(jumpline)