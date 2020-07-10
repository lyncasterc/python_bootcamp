# index - finds the index of an item in a list

numbers = [1, 2, 3, 4, 5 ,6, 7, 8]

print(numbers.index(8))

# can also specify to look for the item, after a certain index

animals = ['cat', 'dog', 'mouse', 'wolf', 'dog', 'zebra']
print(animals.index('dog', 1)) #looks for dog after animals[1]

# count - returns the number of times x is in the list

print(animals.count('dog'))

# reverse - reverses the order in the list

animals.reverse()

print(animals)

# sort - sorts items in ascending order (numerically or alpabetically, etc)

numbers2 = [1, 4, 10, 5, 100, 3]

numbers2.sort()

print(numbers2)

# join - not a list method, but it combines string in a list

words = ['sup', 'bitch']

print(''.join(words)) 

# join adds whatever is in the string between the strings being combined

print(' '.join(words)) 

