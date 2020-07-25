import random 


def roll_dice():

  input("Hit enter to roll dice ")

  dice_choice = random.choice(range(1,6))

  print(dice_choice)

  roll_again = 'y'

  while roll_again == 'y':
    roll_again = input('Do you want to roll again? (y/n)')
    if roll_again == 'y':
      dice_choice = random.choice(range(1,6))
      print(dice_choice)
    else:
      break 

roll_dice()