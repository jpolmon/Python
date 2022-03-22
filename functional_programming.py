# Pure functions - given the same input it will always return the same output and should not have any side effects. 

def multiply_by2(li):
  new_list = []
  for item in li: 
    new_list.append(item*2)
  return new_list

print(multiply_by2([1,2,3]))

# Pure functions usually lead to less bugs in your code.

# In funtional programming you keep the data and functions separate from eachother.

# Map - will perform a funciton over a given iterable data set
# Filter - will remove items based on the requirements
# Zip - will combine two iterables
# Reduce - lets you shrink a list into a single value

# Lambda functions - anonymouse functions that are only used once and not kept in memory

from functools import reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30]

def multiply_by2(item):
  return item*2

def only_odd(item):
  return item % 2 != 0

def sum(running_total, item):
  return running_total + item
  
print(list(map(multiply_by2, my_list)))
print(list(map(lambda item: item*2, my_list)))
print(my_list)
print(list(filter(only_odd, my_list)))
print(list(zip(my_list, your_list)))
print(my_list)
print(reduce(sum, my_list, 0))

# Lambda function exercise

my_list = [5, 4, 3]

print(list(map(lambda num: num**2, my_list)))

# Sort by second number
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key = lambda x: x[1])
print(a)

# Comprehensions can be used to create data structures fast.

# list, set, dictionary

my_list = [char for char in 'hello']
my_list2 = [number for number in range(0,100)]
my_list3 = [num**2 for num in range(0,100)]
my_list4 = [num**2 for num in range(0,100) if num % 2 == 0]

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

# You can do sets the same way that lists are done above

simple_dict = {
  'a': 1,
  'b': 2
}

my_dict = {key:value**2 for key,value in simple_dict.items() if value%2==0}
my_dict1 = {num: num*2 for num in [1, 2, 3]}

print(my_dict)
print(my_dict1)

# Comprehension exercise

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([letter for letter in some_list if some_list.count(letter) > 1]))

print(duplicates)