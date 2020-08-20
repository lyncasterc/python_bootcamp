
# returns the sum of the numbers between 0 and 1000 that are divisble by 3 or 5.
print(sum(num for num in range(0,1000) if num % 3 == 0 or num % 5 == 0))