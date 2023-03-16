def get_population():
  keys = ['col', 'bol']
  values = [300, 400]
  return keys, values

def jumpline():
  print('=' * 30)

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result