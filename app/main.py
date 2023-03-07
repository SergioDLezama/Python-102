'''
Cualquier archivo .pypuede ser un modulo
Para llamar un modulo import
'''
import utils

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