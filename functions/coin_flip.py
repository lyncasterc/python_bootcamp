from random import random

def flip_coin():
 r = random() #generates a random number between 0 and 1, not including 1
 if r >0.5:
   return 'Heads'
 else:
    return "Tails"

print(flip_coin())