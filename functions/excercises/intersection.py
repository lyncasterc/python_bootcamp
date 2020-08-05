def intersection(l1, l2):
  return [val for val in l1 if val in l2]


l1 = ['Boop', 'Boob']
l2 = ['Poop', 'Boob']

print(intersection(l1,l2))