'''

import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
      print('***' * 5)
      print(row) 
'''
#El resultado da una serie de listas, pero es dificil de trabajarlo, vamos a pasarlo a listas de diccionario
'''

def read_csv_2(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    #print(header)
    data = []
    for row in reader:
      #print('\n', '***'*25)
      iterable = zip(header,row)
      #print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data
      
if __name__ == '__main__':
  data = read_csv_2('./data.csv')
  print(data[0])

'''
import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])