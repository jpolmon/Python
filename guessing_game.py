# # import sys 
# from random import randint

# low = int(sys.argv[1])
# high = int(sys.argv[2])
# answer = randint(low, high)

# while True:
#   try:
#     guess = int(input(f'Please guess a number from {low} to {high}: '))    
#     if guess > high or guess < low:
#       raise Exception('Input out of range')
#   except ValueError:
#     print('Please enter a number!')
#   except:
#     print('Please enter a number within the range!')
#   else:
#     print(guess, answer)
#     if guess == answer:
#       print(f'{guess} was the correct answer!')
#       break
#     else:
#       print(f'{guess} was incorrect!')
#       continue

def guessing_game(guess, answer):
  if 0 < guess < 11:
    if guess == answer:
      return 'Correct!'
  else: 
    return 'Hey, it\'s supposed to be 1~10'
