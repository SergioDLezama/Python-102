'''
Cap 29 Paquetes
Importo el paquete pkg y para importar sus funciones y modulos
'''
import pkg
'''
# Forma 1
from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4

print(func_1())
print(func_2())

print(func_3())
print(func_4())
'''
# Lo que este definido en init puedo usarlo al importar el paquete
import pkg

print(pkg.URL)

# Este codigo funciona por que en la linea 8 esta definido
print(pkg.mod_1.func_1())

# Para que funcione sin esa linea, tendria que definir el import en init