import math
from primality import is_prime



def prime_number_generator(limit):
  prime_nums = []

  for n in range(1,limit):
    
    if is_prime(n):
      prime_nums.append(n)

      if n > limit:
        prime_nums.pop()
        break
  
  return prime_nums



print(prime_number_generator(2000000))