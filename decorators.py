# Decorators - such as @classmethod and @staticmethod, they give functions extra features.

def hello():
  print('helllooooo')

greet = hello
del hello #this does not delete the function, only the name reference to it

greet()

# Functions can be passed and act like variables

def hello1(func):
  func()

def greet1():
  print('still here!')

a = hello1(greet1)

print(a)

# Highter Order Function is a function that accepts a function as a parameter or returns a function.

# Below is the decorator pattern, this allows you to enter pass any number of variables. 

def my_decorator(func):
  def wrap_func(*args, **kwargs):
    print('********')
    func(*args, **kwargs)
    print('********')
  return wrap_func

@my_decorator
def hello(greeting, emoji=':('):
  print(greeting, emoji)

# @my_decorator
# def bye():
#   print('see ya later')

hello('hiiii')
# bye()

# Practical applications of decorators

# This decorator allows you to determine the performance of any function you make

from time import time

def performance(func):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = func(*args, **kwargs)
    t2 = time()
    print(f'Function took {t2-t1} s to run')
    return result
  return wrapper

@performance
def long_time():
  for i in range(1000000):
    i*5

long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  # code here
  def wrap_func(*args, **kwargs):
    if True in args[0].values():
      fn(*args, **kwargs)
  return wrap_func

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)