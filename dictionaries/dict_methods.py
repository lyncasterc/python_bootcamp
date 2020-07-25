
stiven = {
  'is_math_genius': True,
  'is_science_genius': True,

}

print(stiven)

#.clear() - deletes all keys and values in the dictionary, returns a totally empty dictionary
# stiven.clear()

# print(stiven) 

#  .copy() = makes a copy of the keys and values from a dict.
stiven_evil_twin = stiven.copy()

print(stiven_evil_twin)

# {}.fromkeys([]) is usually used to set starting default values like in a game or profile. Creates a new dictionary.
# you pass in a list of strings which are the keys, then what you want each key's value to be. You can either create the list right in the method or pass in a list's name

boop = ['name', 'age', 'email']

# these do the exact same thing.

{}.fromkeys(boop, 'unknown')
{}.fromkeys(['name', 'age', 'email',], 'unknown')

# .get() retrieves a key from a dict, and if the key doesn't exist, returns None instead of an error
stiven.get('is_math_genius')


# d.pop() - removes a key-value pair. d represents the name of the dictionary, then .pop('a') such that a is the key name of the key-value pair you wish to remove 

d = {
  'a': 1,
  'b': 2,
  'c': 3
}
# print(d)
# d.pop('a')

# print(d)

# d.popitem() - removes a random key-value pair from the dicionary; no argument passed in

e = {
  'd': 6,
  'a': 2, #this will get overwriten 
}
print(e)
# this takes the key-value pairs from one dictionary and copies it into another, will overwrite any identical key in the dictionary being copied into.
e.update(d)

print(e)
