def average_age_calc(num_list):
  age_sum = 0

  for num in num_list:
    age_sum += num
  
  average_age_result = (age_sum)/len(num_list)
  return average_age_result





def average_age():
  ages_list = []

  age = input('Enter the person\'s age: ')
  print('Enter n at any time to calculate average age of the ages entered.')

  while age != 'n':
    age = int(age)
    ages_list.append(age)
    age = input('Enter next age: ')

    if age == 'n':
      num_of_ages = len(ages_list)
      result = average_age_calc(ages_list)

      print(f'You entered {num_of_ages} ages')
      print(f"The average age is {result} ")
      
      
      break


average_age()




  
    







