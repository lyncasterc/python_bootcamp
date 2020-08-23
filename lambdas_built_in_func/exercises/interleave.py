def interleave(str_1,str_2):
  zipped_str = list(zip(str_1,str_2))
  boop= []

  for pair in zipped_str:
    boop.append(pair[0])
    boop.append(pair[1])

  
  return ''.join(boop)
  
  
  




print(interleave('hi','ha'))
