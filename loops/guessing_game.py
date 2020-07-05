import random

keep_playing = 'y'


while keep_playing == 'y':
 
  random_number = random.randint(1, 10)

  user_guess = int(input('Guess a number between 1 and 10: '))
  
  while user_guess != random_number:
    if user_guess > random_number:
      print('Too high, try again!')
      user_guess = int(input('Guess a number between 1 and 10: '))
    if user_guess < random_number:
      print('Too low, try again!')
      user_guess = int(input('Guess a number between 1 and 10: '))
  if user_guess == random_number:
    print('You guessed it! You won!')
    keep_playing = input('Do you want to keep playing (y/n) ')
    if keep_playing == 'n':
      break
print('Thanks for playing! Bye!')
  
