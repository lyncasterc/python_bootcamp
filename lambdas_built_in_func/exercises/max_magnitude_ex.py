nums = [1,-2,3,4,-5]

# print(max([abs(i) for i in nums]))




# this function returns back the max absolute value in a list of numbers

# the functions takes a list a numbers. A list comprehension is run to return the abs value of each element in the list, which produces of list of the abs values.
# that list is then passed into max, which returns the max abs value.
def max_magnitude(l):
  return max([abs(i) for i in l])


print(max_magnitude(nums))

