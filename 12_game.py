import random
import os
'''
El proyecto es hacer un juego de consola de 
Piedra, Papel o Tijera

Vamos a anadir funciones
       
'''

jumpline = '\n'

line = '=' * 25

def game_init():
  os.system('clear')
  print(input(line + '\nBIENVENIDO A PIEDRA PAPEL O TIJERA!!!\nQUE GANE EL MEJOR DE 3!!\nPRESIONA [ENTER] PARA EMPEZAR\n' + line + jumpline))
  
def choose_option():  
    options = ('piedra', 'papel', 'tijera')
    user_option = input('\nPiedra, papel o tijera?: ').lower()
    computer_option = random.choice(options)
    
    '''
    # Esta linea confirma que el user de una de las opciones posibles
    if not user_option in options:
      print(input('\nEsa opcion no es valida\nPRESIONA [ENTER] PARA REINTENTAR'))
      choose_option()
      #return user_option, computer_option
      #continue
    '''
    
    return user_option, computer_option

def game_rules(user_option, computer_option, user_wins, computer_wins):
  
  if user_option == computer_option:
    print(f'\n"{user_option.upper()}", Empate!!')
  
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('\n"TIJERA", Ganaste!')
      user_wins += 1
    else:
      print('\n"PAPEL", Perdiste!')
      computer_wins += 1
  
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('\n"PIEDRA", Ganaste!\n')
      user_wins += 1
    else:
      print('\n"TIJERA", Perdiste!\n')
      computer_wins += 1
  
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('\n"PAPEL", Ganaste!\n')
      user_wins += 1
    else:
      print('\n"PIEDRA", Perdiste!\n')
      computer_wins += 1
  else:
    print('Opcion no valida!')
  print(input('\nSiguiente ronda! Presiona ENTER\n'))
  return user_wins, computer_wins

def run():
  computer_wins = 0
  user_wins = 0
  counter = 1
  game = True
  
  while game:
    
    os.system('clear')
    print('='*25)
    print(f'ROUND {counter}')
    print('='*25)
    print(f'PUNTOS\nUSUARIO {user_wins}\nCOMPUTER {computer_wins}')
    print('='*25)
        
    #print(jumpline ,'User options: ', user_option.title())
    #print('Computer uption: ', computer_option.title(), jumpline)
    
    user_option, computer_option = choose_option()
    user_wins, computer_wins = game_rules(user_option, computer_option, user_wins, computer_wins)
    
    if user_wins == 3:
      os.system('clear')
      print(input('USUARIO GANA!!!!!\n'))
      game = False
    elif computer_wins == 3:
      os.system('clear')
      print(input('COMPUTER GANA!!!!!\n'))
      game = False
      
    counter += 1

if __name__ == '__main__':
  run()