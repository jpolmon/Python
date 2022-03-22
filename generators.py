# Generators - such as range()

range(100)
list(range(100))

def make_list(num):
  result = []
  for i in range(num):
    result.append(i*2)
  return result

my_list = make_list(100)
print(my_list)

# All generators are iterable

def generator_function(num):
  for i in range(num):
    yield i

g = generator_function(100)
next(g)
next(g)
print(next(g))

print(next(g))
# for item in generator_function(1000):
#   print(item)

# Creating our own generators

def special_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      print(iterator)
      next(iterator)
    except StopIteration:
      break

special_for([1, 2, 3])

# How generators work under the hood

class MyGen():
  current = 0
  def __init__(self, first, last):
    self.fisrt = first
    self.last = last

  def __iter__(self):
    return self

  def __next__(self):
    if MyGen.current < self.last:
      num = MyGen.current
      MyGen.current += 1
      return num
    raise StopIteration
  
gen = MyGen(0,100)
for i in gen:
  print(i)

# Creating a Fibonacci sequence

def fib(num):
  prev1 = 1
  prev2 = 0
  for i in range(num):
    yield prev2
    temp = prev1 + prev2
    prev2 = prev1
    prev1 = temp
      
for number in fib(21):
  print(number)