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