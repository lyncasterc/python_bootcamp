def isEven(num):
  return num % 2 == 0

def partition(num_list, func):
  
  truthy_list = [num for num in num_list if isEven(num)]

  falsy_list = [num for num in num_list if isEven(num) != True]
  
  return [truthy_list, falsy_list]



num_list = [1,2,3,4,5]
print(partition(num_list, isEven))