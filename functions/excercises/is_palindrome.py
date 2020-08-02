def is_palindrome(word):
	word = word.lower().replace(' ','')
	return word[::-1] == word



    

word = input("enter a word: ")
print(is_palindrome(word))

# Notes - 
# You can use multiple methods in one line
# .replace('x', 'y')  can be called on a string and you pass in want you want to replace in x and what it sould be replaced by in y.