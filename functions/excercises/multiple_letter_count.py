def multiple_letter_count(word):
  word = word.lower()
  print(word)
  return {letter:word.count(letter) for letter in word}

print(multiple_letter_count('Bobobobobobob'))