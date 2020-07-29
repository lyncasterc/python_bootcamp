# variables defined inside functions are scoped to local which means they can only be used inside that function and no where else.

# global variables can be used anywhere, but can't be changed inside functions unless you specify inside the function to use a the global scope varibable

total = 0

def increment():
  global total #this tells python to use the global scope variable. w/o this, it wouldn't work.
  total += 1
  return total

  