is_magician = False
is_expert = True

# check if magician AND expert: "you are a master magician"

# check if magician but not expert: "at least you're getting there"

# if you're not a magician: "You need magic powers"

if is_magician and is_expert:
  print("You are a master magician")
elif is_magician and not is_expert:
  print("At least you're getting there")
elif not is_magician:
  print("You need magic powers")

print(True == 1) # True
print('' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([] == []) # True

print(True is 1) # True
print(1 is 1) # False
print([] is 1) # False
print(10 is 10.0) # True
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # True
b = a
print(a is b)

# is checks for location in memory