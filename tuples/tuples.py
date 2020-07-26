# ordered collection of items
# difference between list and tuples is that tuples are immutable, cannot be changed

numbers = (1,2,3,4)

# if you tried to change of value of numbers like:
numbers[0] = 2 #returns an error

# tuples are faster than lists. If you know you have a list of things that won't ever change, it can be better to use tuples

# it can also make your code safer from bugs

# an example to use them would be months of the year

# you can use tuples as keys in dictionaries (imagine the random numbers are lat and long coordinates, which would obv never change)
locations  = {
  (101010, 101010):'NYC',
  (1010101, 100008):'Tokyo',
  (2030, 230582): 'SF',

}