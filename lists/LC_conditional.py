numbers = [1, 2, 3, 4, 5, 6]

even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

print(even)
print(odd)

new_list = [num * 2 if num % 2 == 0 else num / 2 for num in numbers]

print(new_list)