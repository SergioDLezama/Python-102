'''
Cualquier archivo .pypuede ser un modulo
Para llamar un modulo import
'''
import utils
'''
Para que no se ejecute todo el archivo voy a modularlo
con una funcion

keys, values =utils.get_population()
print(keys, values)
utils.jumpline()

data = [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

country = input('Type Country: ').title()

result = utils.population_by_country(data, country)
print(result)
'''
data = [
    {
      'Country': 'Colombia',
      'Population': 500
    },
    {
      'Country': 'Bolivia',
      'Population': 300
    }
  ]
  
'''
Con el codigo en una funcion puedo importarlo como un script PERO ya no puedo correrlo
como un script asi que le coloco un entrypoint
'''
def run():
  keys, values =utils.get_population()
  print(keys, values)
  utils.jumpline()
  
  country = input('Type Country: ').title()
  
  result = utils.population_by_country(data, country)
  print(result)

# Si es ejecutado desde la terminal, corre la funcion run, sino no hagas nada
if __name__ == '__main__':
  run()

