# ** arguments will unpack dictionaries
# same idea as *args, but with dics instead of tuples and lists

def display_names(first, second):
  print(f"{first} says hello to {second}")


names = {'first': 'emilia',
'second': 'stiven'}

display_names(**names)
# emilia says hello to stiven



