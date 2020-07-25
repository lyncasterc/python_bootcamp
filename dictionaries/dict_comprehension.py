num = {
  'first':1,
  'second':2,
  'third':3
}

# this is dictionary comprehension. iterates over dictionaries, keys by default and you can do both key and value with .items().
squared_num = {key:value ** 2 for key,value in num.items()}

print(squared_num)


# this creates a dictionary, starting with a list. num is assigned to each number in the list and then creates a dictionry with num as the key and num squared as the value
more_squared_num = {num: num ** 2 for num in [1,2,3,4,5]}

print(more_squared_num)

instructor = {
  'name': 'Colt',
  # 'owns_dog': True,
  'num_of_courses': '4',
  'fav_language': 'Python',

}

# this iterates over every key and value in instructor and makes them both uppercase.
yelling_instructor = {key.upper():value.upper() for key,value in instructor.items()}

print(yelling_instructor)


# Conditional logic

num_list = [1,2,3,4]

# assigns num to each number in the list, then creating dictionary with num as key and the in parenthesis asssigning the value to even if it's even or else odd. 
print({num: ('even' if num % 2 == 0 else 'odd') for num in num_list})
