# map is a standard built in function.
# accepts at least two argument - an iterable, and a function, usually a lambda.
# it takes each element in the iterable and runs the function

nums = [1,2,3,4]



print(list(map(lambda x: x *2 ,nums))) #this takes a list of numbers and runs the lambda over each element in the list, doubling them


names = [
  {'first': 'Stiven', 'last': 'Cabrera'},
  {'first': 'Emilia', 'last': 'Telfer-Cabrera'},
  {'first': 'Liara', 'last': 'Cabrera'},
]

print(list(map(lambda name : name['first'].upper(),names)))

