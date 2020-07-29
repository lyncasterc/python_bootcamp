def list_manipulation(list1, command, location, value=None):

  if command == 'remove':
    if location == 'end':
      return list1.pop()
    elif location == 'beginning':
      return list1.pop(0)
  elif command == 'add':
    if location == 'beginning':
      list1.insert(0, value)
      return list1
    elif location == 'end':
      list1.append(value)
      return list1


 
num = [1,2,3]

print(list_manipulation(num, 'add', 'end', 'cat'))