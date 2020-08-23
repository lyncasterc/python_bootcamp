# dividend = 1
divisors = [11,13,14,16,17,18,19,20]
# l = [1,2,3,4,5,6,7,8,9,10]


def find_solution(step):
  for dividend in range(step,999999999,step):
    if all(dividend % i ==0 for i in divisors):
      return dividend

print(find_solution(2520))




# i had code that worked but took too long.
# The solution to make this run quicker was to realize that is we leave 20 in, 
# any num divisble by 20 is also disible by 2. So we take 2 our. 19 is prime, so it's left in. 
 






