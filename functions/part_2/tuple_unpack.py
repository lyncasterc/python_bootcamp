# you can use * as an argument to unpack values

def sum_all_nums(*args):
  sum = 0

  for i in args:
    sum += i

  print(sum)
  return sum

    # in this example function, you enter several numbers as arguments and it will add up the numbers
    # But if you tried to enter a list of numbers to be added, it wont work unless you add *before passing in the list name.

  
nums = [1,2,3,4,5]

sum_all_nums(*nums) 

