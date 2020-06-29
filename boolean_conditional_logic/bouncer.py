def bouncer():
  
  normal_entry = None
  wristband_entry = None
  no_entry = None
  
  age = input('How old are you? ')
  while age == "":
    age = input('Error! Enter your age in years: ')
  else:
    if int(age) >= 18:
      if int(age) >= 21:
        normal_entry = True
        print('Drink, normal entry')
      else:
        wristband_entry = True
        print('Wristband') 

    else:
      no_entry = True
      print('No entry, minimum age for entry is 18.')
    
    return (normal_entry, wristband_entry, no_entry)

bouncer()