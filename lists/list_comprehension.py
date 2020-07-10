nums = [1, 2, 3]
new_nums = [x * 10 for x in nums]
print(new_nums)

# states that x is being multiplied by 10, then assigns x to the values in nums. 
# it loops through the list, assigning each value to x, multipying by 10, then repeating with the next value
# returns a new list

name = 'Stiven'

print([x.upper() for x in name])

couple = ['stiven', 'emilia']

print([x[0].upper() + x[1:] for x in couple])
# defines x as each item in couple, which are two strings 
# so x[0] is the first letter of each string.
# x[0].upper() is capatlizing the first letter of each string
# x[1:] is every letter in each string after the first.
# x[0].upper() + x[1:] concatenates the capitalized first letter, put every other letter, returning 'Stiven', 'Emilia'

print([num * 10 for num in range(1,6)])

# defines num as range(1,6), and loops through and multiplies num by 10.

numbers = [1, 2, 3, 4, 5, 6]

string_list = [str(num) for num in numbers]

print(string_list)

