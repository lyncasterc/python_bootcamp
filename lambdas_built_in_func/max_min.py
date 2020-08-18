# max - returns largest item in iterable

num = [2,3,3,4,6]

print((max(num))) #will return 6

# min - does the opposite

names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(min([len(name) for name in names])) #returns length of shortest name in the list

print(max(names, key=lambda name: len(name) ))
#returns actual longest name