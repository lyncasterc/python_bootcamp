'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''
# function takes in two numbers and compares them 
def number_compare(num1,num2):
  if num1 == num2:
    return 'Numbers are equal'
  elif num1 > num2:
    return 'First is greater'
  return 'Second is greater'

print(number_compare(2,2))