# foobar
# the above line of code would return an error and break the program because it's an undefined variable

# try:
#   foobar
# except NameError:
#   print('error') 

#  this would try and see if foobar is in the code, which it isn't. instead of returning an error which breaks the whole thing, it runs the code in except and then moves on to execute the rest of the program

d = {"name":"Ricky"}

def get(d,key):
  try:
    return d[key]
  except KeyError:
    return None

print(get(d,"city"))



try:
  num = int(input('enter a number: '))
except ValueError as err:
  print('you didn\'t enter a number')
  print(err)
else:
  print('lol')
finally:
  print('lol x2')
  

# else - the code in else runs when except doesn't run
# finally - code in this block runs no matter what


def divide(a,b):
    try:
        total = a / b
    except TypeError:
        return "Please provide two integers or floats"
    except ZeroDivisionError:
        return "Please do not divide by zero"
    return total

print(divide(1,0))

