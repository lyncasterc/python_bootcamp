# append - adds item to end of list

numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers) 
# prints [1, 2, 3, 4, 5]

# extend -  adds several items to the end of a list

numbers.extend([6, 7, 8, 9])

print(numbers)

# insert - can add item at given position, take the place of the index you pass in

numbers.insert(2, 'boob')
print(numbers)

# clear - removes all items in list at once

# pop - removes item at index passed, or if nothing is passed in, removes last item.

numbers.pop()
print(numbers)

# pop also returns the value removed.

item = numbers.pop(2) #item removed can be stored in a variable
print(item, numbers)

#  remove - takes a value, not an index, and removes the first value equal to what was passed in

numbers.remove(8)
print(numbers)

