# zip
# if you have two lists of the exact lenghth, zip will pair up all the numbers 
# you can zip more than two iterables

# have to convert to list - returns list of  tuples
num1 = [1,2,3]
num2 = [4,5,6]

print(list(zip(num1, num2))) #returns [(1, 4), (2, 5), (3, 6)]


midterms = [80,91,78]
finals = [98,89,53]
students = ['dan','ang','kate']

# say you wanted to pair up each sudent name with their highest grade in either the midterm or final.



final_grades = { pair[0]: max(pair[1], pair[2]) for pair in zip(students, midterms,finals)} 

print(final_grades)





