# tool that allows to make copies of entire or portions (slices) of a list.

# first parameter is where to start slicing from

first_list = [1, 2, 3, 4, 5]
print('start at index 1, inclusive', first_list[1:]) #cuts everything from index of 1, which is 2, and everything after it

# You can also start backwards with negative numbers. -1 would give the last element in the list

# first_list[0:] gives a copy of the list. Not the same list itself, but a copy

# second parameter of slice is end point. Where to end the slice, and exclusive

print('end at index of 2, not including index of 2', first_list[:2]) 
# putting  colon before is indicating to start at index of 0. It's the same as saying first_list[0:2]

# this returns 1, 2.  Doesn't include index of 2, which in this list would be 3.

print(first_list[:3])

# third parameter is step, the number to count at a time 

print('start at index of 1, skip 2', first_list[1::2])
# double colon means no end. This starts at index 1, and then counts every 2.

# negative step reverses order 

print(first_list[2::-1]) 
# this starts at index 2, which is 3, then index 2, counts backwards in steps of 2. Retuns 3, 1
