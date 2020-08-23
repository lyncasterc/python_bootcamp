def triple_and_filter(l):
  return [ num*3 for num in list(filter(lambda num: num%4==0,l))]


num = [1,2,3,4]
print(triple_and_filter(num))

'''
triple_and_filter([1,2,3,4]) # [12]
triple_and_filter([6,8,10,12]) # [24,36]
'''
