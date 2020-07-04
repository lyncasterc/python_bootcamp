#you can think of range as a slice of the number line 
#range(7) would give you a range between integers 0 and 7, not including 7.
#range(1,8) woulld give you numbers from 1 to 7, and doesn't include 8.
# range(1, 10, 2) would start at one and then skip two numbers.
# range(7, 0, -1) goes backwards from 7 to 0, going down -1 each time.


# for num in range(10):
#   print(num) 

x = 0

for num in range(10, 20):
  if num % 2 != 0:
    x += num
    print(x)

    

