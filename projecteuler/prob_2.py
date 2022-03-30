

# this function takes an number, then calculuates the fibonacci sequence until the last number before the it goes over input
# it returns the list of fibonacci numbers and the sum of the even numbers.
def fibonacci_seq(i):
  fibonacci = [1,2]
  even_sum = 0
  increment = 1
  increment2 = 0

  while even_sum < i:
    even_sum = fibonacci[increment2] + fibonacci[increment]
    fibonacci.append(even_sum)
    increment +=1
    increment2 += 1
  
  if even_sum > i:
    fibonacci.pop()

  return fibonacci, sum(i for i in fibonacci if i % 2 == 0)

print(fibonacci_seq(10000))





