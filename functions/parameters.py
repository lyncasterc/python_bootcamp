# functions can take parameters in the method definition

def square(num):
  return num ** 2

print(square(11))

# can take more than one parameter,depending on the need

def add(num1, num2):
  return num1 + num2

print(add(5,6))

# for default parameter value, set it equal to desired default in paranthesis when defining function
def exponent(num, power=2):
  return num ** power
  
print(exponent(2))






