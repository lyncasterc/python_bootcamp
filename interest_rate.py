import math
def simple_interest_rate():

  principal = float(input('Enter principal '))

  time = float(input('Enter time '))

  rate = float(input('Enter rate '))

  A = principal*(1+rate*time)

  print(f"Final amount is ${round(A,2)}")

  return round(A,2)

# simple_interest_rate()

def continous_interest():
  principal = float(input('Enter principal '))
  time = float(input('Enter time '))
  rate = float(input('Enter rate '))

  A = principal * math.e ** (rate*time)
  
  

  print(f'Final amount is ${round(A, 2)}.')
  return round(A,2)


# continous_interest()



