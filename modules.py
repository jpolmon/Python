# Use import in front of the files name you want to use functions from 

# You can also use 'from "module name" import "function name(s)"' to avoid having to use additional dot notation for all files.

# You can rename the module with 'import "module name" as "module name you wish to give it"'

# dot notation is used for nested modules

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

#you need __init__.py inside of a package

import random

print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4, 5]))