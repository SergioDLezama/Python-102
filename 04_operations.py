jumpline = '-' * 25

set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}
print('SET A => ',set_a) # {'col', 'mex', 'bol'}
print('SET B => ',set_b) # {'pe', 'bol'}
print(jumpline)

# Puedo unir dos sets con .union()
set_c = set_a.union(set_b)
print(set_c) # {'col', 'pe', 'mex', 'bol'}

# Tambien puedo unir dos sets con |
print(set_a | set_b) # {'col', 'pe', 'mex', 'bol'}
print(jumpline)

# Puedo interceptar los elementos en comun con .intersection()
set_d = set_a.intersection(set_b)
print(set_d) # {'bol'}

# Igualmente el singno & hace la funcion de intersection
print(set_a & set_b) # {'bol'}
print(jumpline)

# El metodo de operacion .difference() me retorna los elementos del set a que no esten en el set b
set_e = set_a.difference(set_b)
print(set_e) # {'col', 'mex'}

# Tambien puedo hacer la diferencia con el signo -
print(set_a - set_b)  # {'col', 'mex'}
print(jumpline)

# El metodo Symmetric Difference nos retorna una union sin los elementos en comun
set_f = set_a.symmetric_difference(set_b)
print(set_f) # {'col', 'pe', 'mex'}

# Tambien puedo tener el Symmetric Difference con el signo ^
print(set_a ^ set_b) # {'col', 'pe', 'mex'}
