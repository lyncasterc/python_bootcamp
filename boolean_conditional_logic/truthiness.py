#Certain things in python have inherit truth or false values. 

#empty strings, None, zero, empty objects are exmamples of things that are naturally falsy.

if 0: #if zero is true
  print('yeaaaaaah boiiiiii') 

else:
  print(':(')

  #it prints else because 0 is naturally falsy not truthy


fav_animal = input('What is your favorite animal? ')

if fav_animal: #if fav_animal has any string in it, then it's true.
  print(f'{fav_animal}s are my favorite animal too!')

else: #if fav_animal is empty, then it's not true.
  print('Ya didn\'t type anything, ya dingus')

    