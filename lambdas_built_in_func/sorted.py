# similar to sort list method.
# sorted can also sort other kinds of iterables.

num = [2,4,7,9,0,1]
num2 = [2,4,7,9,0,1]

num.sort() #when you run the sort list method, it sorts the original list

sorted(num2) #sorted does not sort original list - it returns a copy of the list which is sorted

print(num) #returns a sorted list

print(num2) # will not return a sorted list since sorted does not affect origial list

print(sorted(num2)) #returns copy of list, sorted


# we can also reverse the order of sorting to descending 

print(sorted(num2, reverse=True))

# say we want to sort this by the usernames alphabetically

users = [
  {'username': 'bob', 'tweets': ['hi guys', 'boobs']},

  {'username': 'sally', 'tweets': []},

  {'username': 'dave', 'tweets': ['hi guys', 'boobs']}
]


print(sorted(users, key=lambda user: user['username'] ))