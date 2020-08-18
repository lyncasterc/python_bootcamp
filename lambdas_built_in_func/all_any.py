# built-in func - takes interable and returns True if all elements in the iterable are truthy or empty


l = [0,1,2,3,4,5]

print(all(l)) #this returns false because 0 is not truthy

names = ['kat','kiki','keller']

all([name[0]== 'k' for name in names]) #the list comprehension checks if each element in names starts with k. It returns a list of Truthy or Fasly value. Then all checks returns True if all elements are true

#in essence, the list comprehension passed into all() is checking if the all the elements in the list are something.

 

# any 

# checks if any element is truthy
