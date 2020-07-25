# accessng the values in a dictionary

instructor = {
  'name': 'Colt',
  'owns_dog': True,
  'num_of_courses': 4,
  'fav_language': 'Python',

}
# accesses all the values
for value in instructor.values():
  print(value)

# accesses all the keys
for key in instructor.keys():
  print(key)

# accesses both keys and values
for k,v in instructor.items():
  print(f'{k}: {v}')

