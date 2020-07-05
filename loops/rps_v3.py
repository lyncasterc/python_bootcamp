def rps_v3_start(): 
  player_wins = 0
  computer_wins = 0
  
  while player_wins < 2 and computer_wins < 2:
    print(f'Computer Score: {computer_wins} Player Score: {player_wins}')

    import random

    print('... rock ...\n... paper ...\n... scissors ...')

    rps_choices = ['rock', 'paper', 'scissors']

    player_choice = input('(Enter your choice): ')

    if player_choice == 'quit' or player_choice == 'q':
      break
    
    computer_choice = random.choice(rps_choices)
    
    while player_choice not in rps_choices:
      print('You didn\'t enter rock, paper or scissors!')
      player_choice = input('(Enter your choice): ')

    if player_choice == computer_choice:
      print('SHOOT!')
      print('It\'s a draw!')

    elif player_choice == 'rock':
      if computer_choice == 'paper':
        computer_wins += 1
        print('SHOOT!')
        print('You lose!')
      elif computer_choice == 'scissors':
        player_wins += 1
        print('SHOOT!')
        print('You win!')
    
    elif player_choice == 'paper':
      if computer_choice == 'scissors':
        computer_wins += 1
        print('SHOOT!')
        print('You lose!')
      elif computer_choice == 'rock':
        player_wins += 1
        print('SHOOT!')
        print('You win!')

    elif player_choice == 'scissors':
      if computer_choice == 'rock':
        computer_wins += 1
        print('SHOOT!')
        print('You lose!')
      elif computer_choice == 'paper':
        player_wins += 1
        print('SHOOT!')
        print('You win!')
  print(f'FINAL SCORE: Computer Score: {computer_wins} Player Score: {player_wins} ')

  if player_wins > computer_wins:
    print('You won the game!')
  elif computer_wins > player_wins:
    print('You lost the game.')
  elif player_wins == computer_wins:
    print('It\'s a tie!')
rps_v3_start()


