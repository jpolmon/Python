# Exercise: Check for duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
used_characters = {}
duplicates = []

for letter in some_list:
  if some_list.count(letter) > 1:
    if letter not in duplicates:
      duplicates.append(letter)

for letter in some_list:
  if not letter in used_characters.keys():
    used_characters[letter] = 1
  elif used_characters[letter] == 1:
    duplicates.append(letter)

print(duplicates)
