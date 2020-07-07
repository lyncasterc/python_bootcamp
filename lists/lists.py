# lists can contain any kind of info
demo_list = ['bob', True, 8.9999999] 

print(demo_list)

# len can tell you how many items are in list.
print(len(demo_list))

nums = list(range(1, 100))

print(nums)

# You can check if a value is in a list with in

if 'bob' in demo_list: #this returns Boolean, True in this case
  print('Yup')

# Access items in the list with index

demo_list[0] = 'boob'

print(demo_list[0])

# Iterating over the entire list with loops
print('---Loops over the list---')
for x in demo_list: 
  print(x)
