for item in 'Zero to Mastery':
  print(item)

for item in [1, 2, 3, 4, 5]:
  print(item)

for item in (1, 2, 3, 4, 5):
  for element in ['a', 'b', 'c']:
    print(item, element)

# iterable - list, dictionary, tuple, set, string.
# iterable -> one by one check each item in the collection.

user = {
  'name': 'Golem',
  'age': 5006,
  'can_swim': False
}

for item in user.items():
  print(item)

for item in user.values():
  print(item)

for item in user.keys():
  print(item)

for key, value in user.items():
  print(key, value)

# Counter

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0

for el in my_list:
  count += el

print(count)

# Range

print(range(100))
print(range(0, 100))

for num in range(0, 10): # use _ if you want to state that you are not using the variable
  print(num)

for _ in range(0, 10, 2):
  print(_)

for _ in range(10, 0, -1):
  print(_)

for _ in range(2):
  print(list(range(10)))

# Enumerate - useful when you want to have access to the index values in an iterable

for i,char in enumerate('Helllooo'):
  print(i, char)

for i,char in enumerate([1, 2, 3]):
  print(i, char)

for i, char in enumerate(list(range(100))):
  if char == 50:
    print(f'The index of 50 is: {i}')

# While loops 

i = 0
while i < 50: 
  print(i)
  i += 1
  break
else: # else is used when you want a line to be executed only if there isn't a break in the while loop
  print('done with all the work')

while True:
  response = input('say something: ')
  if (response == 'bye'):
    break

# break - exits the current loop
# continue - continues on to the next iteration of the loop
# pass - goes to the next line, ususally only good to use as a placeholder

# GUI Exercice

picture = [
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0]
]

string = ''

for row in picture:
  for val in row:
    if val == 0:
      print(' ', end = '')
      string += ' '
    else: 
      print('*', end = '')
      string += '*'
  print('')
  string += '\n'

print(string)    

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