# DRY (Don't repeat yourself) <- functions are good at this

# parameters used when defining a a function, can be asssigned default values
def say_hello(name='Darth Vader', emoji=':('):
  print(f'helllooooo {name} {emoji}')

# arguments are used when calling a function

# These are positional arguements
say_hello('JP', ':)')
say_hello('Justin', ':)')
say_hello('Kyler', ':)')

# These are keyword arguments, the order doesn't matter. Putting them not in order is considered bad practice.
say_hello(emoji = ':)', name='David')

say_hello()

# Learning return in python

def sum(num1, num2):
  return num1 + num2

total = sum(5, 10)

print(sum(10, total))
print(sum(10, sum(10, 5)))

# Functions should only do one thing really well.

def sum(num1, num2):
  def another_func(num1, num2):
    return num1 + num2
  return another_func(num1, num2)

total = sum(10,20)
print(total)

#Methods vs Functions

# list()
# print()
# max()
# min()
# input()

def some_random_stuff():
  pass

some_random_stuff()

print('hellooooo'.capitalize())

# Methods have to be owned by something, unlike functions

# Docstrings - gives some information about a function that is defined by the user

def test(a):
  '''
  Info: this function tests and prints param a
  '''
  print(a)

test('!!!!')
help(test)
print(test.__doc__)

# Clean code

def is_even(num):
  return num % 2 == 0

print(is_even(52))
print(is_even(51))

# *args and **kwargs

def super_func(name, *args, i='hi', **kwargs):
  total = 0
  print(*args)
  print(args)
  print(kwargs)
  print(name)
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_func('Andy', 1, 2, 3, 4, 5, num1=5, num2=10))

# Rule: params, *args, default parameters, **kwargs 

# Excercise 

def highest_even(li):
  highest_even = 0
  for num in li:
    if num % 2 == 0 and num > highest_even:
      highest_even = num
  return highest_even

print(highest_even([10, 2, 3, 4, 8, 11])) 

# Walrus operator - helps reduce the amount of operations you need to do within a conditional block

a = 'hellooooooooo'

if ((n := len(a)) > 10):
  print(f'too long {n} elements')

while ((n := len(a)) > 1):
  print(n)
  a = a[:-1]

print(a)

# Scope - what variables do I have access to?

total = 100 # <- has global scope

def some_func():
  total2 = 100

if True:
  x = 10

print(x)
print(total2)

# A new scope is only created when you go within a function
# 1 - functions check local scope first
# 2 - then they check the parent local scope
# 3 - if no parents have the variable they check the user-defined global scope
# 4 - if it is not in the global scope then it checks the built-in python scope

# parameters are considered local variables to a function

total = 0

def count(total):
  # global total
  # total += 1
  total += 1
  return total

print(count(count(count(total))))

# nonlocal reaches up and grabs the variable from the parent scope

def outer():
  x = 'local'
  def inner():
    nonlocal x
    x = 'nonlocal'
    print('inner:', x)
  
  inner()
  print('outer:', x)

outer()

