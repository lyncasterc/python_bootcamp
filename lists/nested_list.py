# You can have lists within lists within lists, etc.

nested_list = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

# Acessing nested lists - first target the index of the list you want, then the index of the item within the list.

print(nested_list[0][1])

print(nested_list[2][1])

# printing values in nested loops - first loops through the top list. x becomes each list, then loops through each list in x. 

for x in nested_list:
  for val in x:
    print(val)

[[print(val) for val in l] for l in nested_list]



# the first part of the code creates a list with the numbers 1,2,3. Then the second part of the code outside the nested brackets repeats the list created.
board = [[num for num in range(1,4)] for val in range(1,4)]

print(board)

board2 = [['X' if num % 2 != 0 else 'O' for num in range(1,4)]for val in range(1,4)]

print(board2)

