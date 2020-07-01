def rps_v2_start(): 

  import random

  print('... rock ...\n... paper ...\n... scissors ...')

  rps_choices = ['rock', 'paper', 'scissors']

  player_choice = input('(Enter your choice): ')

  computer_choice = random.choice(rps_choices)

  while  player_choice not in rps_choices:
    print('You didn\'t enter rock, paper or scissors!')
    player_choice = input('(Enter your choice): ')

  if player_choice == computer_choice:
    print('SHOOT!')
    print('It\'s a draw!')

  elif player_choice == 'rock':
    if computer_choice == 'paper':
      print('SHOOT!')
      print('You lose!')
    elif computer_choice == 'scissors':
      print('SHOOT!')
      print('You win!')
  
  elif player_choice == 'paper':
    if computer_choice == 'scissors':
      print('You lose!')
    elif computer_choice == 'rock':
      print('You win!')

  elif player_choice == 'scissors':
    if computer_choice == 'rock':
      print('You lose!')
    elif computer_choice == 'paper':
      print('You win!')



rps_v2_start()


