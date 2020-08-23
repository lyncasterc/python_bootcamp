

def find_solution(num):
  square_of_sum = sum(i  for i in range(1,num+1)) ** 2
  sum_of_squares = sum(i **2 for i in range(1,num+1))

  return (square_of_sum - sum_of_squares)


print(find_solution(100))