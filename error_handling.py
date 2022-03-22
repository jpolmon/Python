# Error Handling
# try:  
#   def hoohoo():
#     di = {'a': 1}
#     di['b']
  
#   hoohoo()
# except:
#   print('it didn\'t work')

while True:
  try:
    age = int(input('What is your age? '))
    10/age
    raise ValueError('hey, cut it out')
  except ZeroDivisionError:
    print('Please enter an age higher than zero')
    break
  else:
    print('Thank you!')
  finally:
    print('Ok, I am finally done')
  print('Can you hear me?')

# def sum(num1, num2):
#   try:
#     return num1/num2
#   except (TypeError, ZeroDivisionError) as err:
#     print(f'Oops {err}')

# print(sum(1, 0))