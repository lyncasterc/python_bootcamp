


# this is a function that returns the nearest prime number of any given number.
# for ex: if you pass in 3, it will return 3. If you pass in 4, it will return 5
def prime_number_generator(divident):
  q = None
  prime_num_divisor=2
  
  if divident == 1:
    return 1

  while prime_num_divisor <= divident:
    q = divident % prime_num_divisor #5 % 2
    if q == 0:
      if prime_num_divisor == divident: #if 2 == 5
        return divident 
      elif prime_num_divisor != divident:  #2 != 5
        divident +=1 
      
    elif q != 0:
      prime_num_divisor += 1 


# this is a function that returns True or False if a given input is prime or not, respectively.
# for ex: 3 = True (bc it is prime)
def prime_number_checker(divident):
  q = None
  prime_num_divisor=2
  is_prime = None

  if divident == 1:
    is_prime = True
  

  while prime_num_divisor <= divident:
    q = divident % prime_num_divisor #5 % 2
    if q == 0:
      if prime_num_divisor == divident: #if 2 == 5
          is_prime = True
          break
      elif prime_num_divisor != divident:  #2 != 5
        is_prime = False
        break
    elif q != 0:
      prime_num_divisor +=1 

  return is_prime


# this is a function that takes an input and returns a list of the prime factors of the input.
# this functions calls the previous two functions and will not work w/o them
def prime_fac(num):
  prime_fac = []
  prime_fac_q = None
  i = 2

  if num == 1:
    prime_fac.append(num)


  while i <= num:

    prime_number = prime_number_generator(i)

    if num % prime_number == 0:
      prime_fac.append(prime_number)

      prime_fac_q = num/prime_number
      

      if prime_number_checker(prime_fac_q) == True:
        prime_fac.append(prime_fac_q)
        

        break
      elif prime_number_checker(prime_fac_q) == False:
        num = prime_fac_q
        
    elif num % prime_number != 0:
      
      i += 1   
      # print(i,prime_number)
      
  
  return prime_fac





