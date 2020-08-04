num_list = [3,2,2,19,2]


def multiply_even_numbers(num_list):
  num_product = 1
  for num in num_list:
    if num % 2 == 0:
       num_product *= num
  return num_product
   



print(multiply_even_numbers(num_list))