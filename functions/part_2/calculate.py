'''
calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"

calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"
'''

# arguments - make_float, operation, message, first,second
def calculate(**kwargs):
  total = 0
  if 'first' in kwargs and 'second' in kwargs:

    if kwargs['operation'] == 'add':
      total = kwargs['first'] + kwargs['second']
      # print(total)
    
    elif kwargs['operation'] == 'subtract':
      total = kwargs['first'] - kwargs['second']

    elif kwargs['operation'] == 'divide':
      total = kwargs['first'] / kwargs['second']

    elif kwargs['operation'] == 'multipy':
      total = kwargs['first'] * kwargs['second']

  if 'make_float' in kwargs and kwargs['make_float'] == True:
    total = float(total)

  if 'message' in kwargs:
    result = '{} {}'
    return result.format(kwargs['message'], total)
  result = 'The result is {}'
  return result.format(total)




print(calculate(first=1,second=2, operation='add', make_float=False))