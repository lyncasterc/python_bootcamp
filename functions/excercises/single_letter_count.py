# this function takes two parameters, a word and a letter. 
# It makes the word lowercase and the string lowercase which makes the function case insensitive
# returns how many times the letter appears in the word

def single_letter_count(word,letter):
  return word.lower().count(letter.lower())

print(single_letter_count('cAtAaTaaTtaa', 'a'))