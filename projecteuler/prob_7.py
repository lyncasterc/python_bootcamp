import math
from primality import is_prime


def prime_number_generator(num):
  prime_nums_list = []
  i=2

  while len(prime_nums_list) != num:
    if is_prime(i):
      prime_nums_list.append(i)
    i+=1 


  return prime_nums_list


print(prime_number_generator(100))


