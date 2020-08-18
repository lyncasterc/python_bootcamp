def sum_floats(*args):
  return sum(i for i in args if type(i)==float)




print(sum_floats(1,2.2,3.3))