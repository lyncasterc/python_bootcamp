# lists can take multiple values in but provide no information concerning what each value is.
# with dictionaries, you can keep related values all in one place.

instructor = {
  'name': 'Colt',
  'owns_dog': True,
  'num_of_courses': 4,
  'fav_language': 'Python',

}

# the left side are called keys and the right side are called values

cat = {
  'name': 'Kitty',
  'age': 1,
  'is_cute': True,

}

print(cat)

# you can also create dictionaries with the dict function

cat2 = dict(name='Olive', age=2)

print(cat2)

# Accessing individual values

print(cat['name'])

artist = {
    "first": "Neil",
    "last": "Young",
}



full_name = f'{artist["first"]} {artist["last"]}'

print(full_name)

full_name2 = artist['first'] + ' ' + artist['last']

print(full_name2)

# both print Neil Young 

# checks if a key is in the dictionary and returns boolean
print('name'in instructor)

# checks if a value is in the dictionary and returns boolean
print(4 in instructor.values())


