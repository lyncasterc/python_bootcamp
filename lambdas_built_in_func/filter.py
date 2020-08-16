# filter is like map\
# it takes a function (or lambda), an iterable and returns the data we want.



nums = [1,2,3,4]

evens = list(filter(lambda num: num % 2 == 0,nums))

# print(evens)

names = ["ash", "bob", "kat", "aaron", "angel"]

a_name = list(filter(lambda name: name[0]== 'a', names))

# print(a_name)

users = [
  {'username': 'bob', 'tweets': ['hi guys', 'boobs']},

  {'username': 'sally', 'tweets': []},

  {'username': 'dave', 'tweets': ['hi guys', 'boobs']}
]

inactive_users = list(filter(lambda user: len(user['tweets']) != 0 ,users))

print(inactive_users)