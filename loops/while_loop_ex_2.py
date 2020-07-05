import random

number = 0

i = 0


while number != 5:
  number = random.randint(1, 10)
  i += 1
  print(i, number)

