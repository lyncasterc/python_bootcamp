# single-star operator, *args

# special operator passed to functions

# gather remainig arguments as tuple


# can be named anything, as long as single star is in front

# def sum_all_nums(num1,num2,num3):

#   return num1+num2+num3

# print(sum_all_nums(1,2,3))

# if you wanted this function to work and add all the numbers added even if more than 3 arguments added, you'd have to add more parameters, add on to the return statement

# but say you only want to add two numbers, the function won't work in that case since it requires more arugments. *args fixes this



def sum_all_nums(*args):
  sum = 0

  for i in args:
    sum += i

  print(sum)
  return sum


sum_all_nums(5,5,5,5,5,5,5,5)


