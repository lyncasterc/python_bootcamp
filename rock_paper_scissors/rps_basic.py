def rps_start():
  
  print('... rock ...\n... paper ...\n... scissors ...')
  
  player_1_choice = input('(Enter Player 1\'s choice): ')
  
  while player_1_choice == '':
    print('You didn\'t enter anything!')
    player_1_choice = input('(Enter Player 1\'s choice): ')
  
  while player_1_choice != 'rock' and player_1_choice != 'paper' and player_1_choice != 'scissors':
    print('You didn\'t enter rock, paper or scissors!')
    player_1_choice = input('(Enter Player 1\'s choice): ')


  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  print('*** NO CHEATING *** ')
  
  player_2_choice = input('(Enter Player 2\'s choice): ')
  
  while player_2_choice == '':
    print('You didn\'t enter anything!')
    player_2_choice = input('(Enter Player 2\'s choice): ')
  
  while player_2_choice != 'rock' and player_2_choice != 'paper' and player_2_choice != 'scissors' :
    print('You didn\'t enter rock, paper or scissors!')
    player_2_choice = input('(Enter Player 1\'s choice): ')


  if player_1_choice == 'rock':
    if player_2_choice == 'paper':
      print('SHOOT!')
      print('Player 2 wins!')
    elif player_2_choice == 'scissors':
      print('SHOOT!')
      print('Player 1 wins!')
    else: 
      print('SHOOT!')
      print('It\'s a draw!')
  
  elif player_1_choice == 'paper':
    if player_2_choice == 'scissors':
      print('SHOOT!')
      print('Player 2 wins!')
    elif player_2_choice == 'rock':
      print('SHOOT!')
      print('Player 1 wins!')
    else: 
      print('SHOOT!')
      print('It\'s a draw!')
  
  elif player_1_choice == 'scissors':
    if player_2_choice == 'rock':
      print('SHOOT!')
      print('Player 2 wins!')
    elif player_2_choice == 'paper':
      print('SHOOT!')
      print('Player 1 wins!')
    else:
      print('SHOOT!')
      print('It\'s a draw!')

rps_start()  
