# gathers keyword arguments as dictionary

# def fav_colors(**kwargs):
#   # print(kwargs) -
#   for person, color in kwargs.items():
#     print(f'{person}\'s favorite color is {color}' )


# fav_colors(stiven='red', emilia='blue')

def combine_words(word, **kwargs):
  if 'prefix' in kwargs:
    full_word = kwargs['prefix'] + word
  elif 'suffix' in kwargs:
    full_word = word + kwargs['suffix']
  else:
    return word
  return full_word
  

print(combine_words("child", prefix="ish"))
