# Fundamental Data Types
# int and float
print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))

print(type(9.9 + 1.1))

print(2 ** 3)
print(5 // 4)
print(6 % 4)

# math functions
print(round(3.9))
print(abs(-20))

# Operator Precedence
print((20 - 3) + 2 ** 2)

# PEMDAS
# ()
# **
# * /
# + -

print(bin(5))
print(int('0b101', 2))

# Strings
long_string = '''
WOW
0 0
---
'''

print(long_string)

first_name = 'JP'
last_name = 'Olmon'
full_name = first_name + ' ' + last_name
print(full_name)

# Type conversion
print(type(str(100)))
a = str(100)

# Escape Sequence
weather = "\t It's \"kind of\" sunny \n hope you have a good day!"
print(weather)

# Formatted Strings

name = 'Johnny'
age = 55

print('hi ' + name + '. You are ' + str(age) + ' years old.')
print(f'hi {name}. You are {age} years old.')

# String Indexes
selfish = '01234567'
          #01234567

# [start:stop:stepover]
print(selfish[::-1])

# Immutability
# selfish[0] = '8' <---- cannot do this
selfish += '8'

print(selfish)

# String Methods
quote = 'to be or not to be'

print(quote.upper())
print(quote.find('be'))
print(quote.replace('be', 'me')) # temporarily creates a new string that isn't stored in memory once the line is ran
print(quote)

#Booleans

name = 'JP'
is_cool = False

is_cool = True

print(bool(1))
print(bool(0))

# Type conversion

birth_year = input('what year were you born?')

age = 2021 - int(birth_year)

print(f'Your age is: {age}')

# Password Checker

username = input('Please enter your username: ')
password = input('Please enter your password: ')

hidden_password = '*' * len(password)
password_length = len(password)

print(f'{username}, your password, {hidden_password}, is {password_length} letters long.')

# Lists

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

amazon_cart = [
  'notebooks', 
  'sunglasses',
  'toys',
  'grapes'
]

amazon_cart[0] = 'laptop' # Lists are mutable
new_cart = amazon_cart[:]
new_cart[0] = 'gum'

print(amazon_cart[0])
print(amazon_cart[1])
print(amazon_cart[0:3])
print(amazon_cart)
print(new_cart)

# Matrix

matrix = [
  [1, 5, 1],
  [0, 1, 0],
  [1, 0, 1]
]

print(matrix[0][1])

# List Methods

basket = [1, 2, 3, 4, 5]

# Not all methods return a new list
# adding
basket.append(100)
basket.insert(5, 100)
basket.extend([100, 101])
print(basket)

# removing
new_list = basket.pop()
basket.pop(0) # index
basket.remove(4) # value
print(basket)
print(new_list)

basket.clear()
print(basket)

# accessing

basket = ['a', 'b', 'c', 'd', 'e']

print(basket.index('d'))
print('d' in basket)
print('x' in basket)
print('i' in 'hi my name is jp')
print(basket.count('d'))

basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']

basket.sort() # modifies the existing list
print(sorted(basket)) # creates a new list but does not modify the existing list
print(basket)

basket.reverse()
print(basket)
print(basket[::-1])

print(list(range(101)))

new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'JOJO'])
print(new_sentence)

# List Unpacking

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)
print(d)

# None, no value similar to Null in JS

weapons = None
print(weapons)

# Dictionary - un-ordered key-value pair

dictionary = {
  'a': [1, 2, 3],
  'b': 'hello',
  'x': True
}

my_list = [
  {
  'a': [1, 2, 3],
  'b': 'hello',
  'x': True
  },
  {
  'a': [4, 5, 6],
  'b': 'hello',
  'x': True
  }
]

print(dictionary)
print(dictionary['b'])

print(my_list[0]['a'][2])
print(dictionary['a'][1])

# Dictionary keys need to be immutable 

user = {
  'basket': [1, 2, 3],
  'greet': 'hello',
  'age': 20
}

user2 = dict(name = 'JonJon')

print(user.get('age', 55))
print(user2)
print('basket' in user)
print('size' in user)
print('age' in user.keys())
print('hello' in user.values())
print(user.items())
user3 = user.copy()
# user.clear()
print(user)
print(user3)
print(user.pop('age'))
print(user.popitem())
print(user.update({'age': 55}))
print(user)

# Tuple - an immutable list, more predicatable and faster but less flexible

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple[1])
print(5 in my_tuple)

# tuples can be used as dictionary keys

new_tuple = my_tuple[1:2]
x, y, z, *other = (1, 2, 3, 4, 5)

print(new_tuple)
print(x)
print(other)

print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))

# Sets - un-ordered collection of unique objects

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))

my_set = {1, 2, 3, 4, 5, 5}
my_set.add(100)
my_set.add(2)
print(my_set)
print(1 in my_set)
print(len(my_set))
print(list(my_set))
new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)