# and - truthy is both sides of the statement are true.
#  if a and b:
#     print(c)

# age = int(input('how old are you? '))

# if age <= 2:
#   print('Free ticket')

# elif age > 2 and age <=10: #only runs if both sides are true
#   print('Child price')

# else: 
#   print('Adult price')

# #or - only one side has to be true

# city = input('What city do you live in? ')
# if city == 'Los Angeles' or city == 'San Francisco':
#   print('You live in California')


#not - logical negation. Truthy is the opposite is true. 
  #In other words, if blank is not true.

is_weekend = False

if not is_weekend: #This is truthy because it's checking if is_weekend is NOT true and it's not.
  print('Go to work')
