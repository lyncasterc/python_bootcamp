# this function takes multiple numbers with *args, and if they are even, are added to a list. the function then returns the sum of all the even numbers. If there are no even numbers, it returns 0



def sum_even_values(*args):
  div_by_two = []
  
  for i in args:
    if i % 2 == 0:
      div_by_two.append(i)
    elif i % 2 == 0:
      return 0
  return sum(div_by_two)
    


# better way of doing this - you can pass in list comprehension syntax into sum to check if the numbers are even, and then it returns the sum

# the default value of sums is 0 so if there are no even numbers, it will return 0.

def sum_even_values_v2(*args):
  return sum(i for i in args if i % 2 == 0)

print(sum_even_values(1,3))
print(sum_even_values_v2(1,2))