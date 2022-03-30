# file = open('text.txt')

# print(file.readlines())

# write mode will create a file if they don't exist

# try: 
#   with open('./sad.txt', mode='w') as file:
#     text = file.write(':(')
#     print(text)
# except FileNotFoundError as err:
#   print('file does not exist')
#   raise err

# Translation Excercise

from translate import Translator

translator = Translator(to_lang='ja')

try:
  with open('text.txt', mode='r') as file:
    text = file.read()
    translation = translator.translate(text)
    print(translation)
    with open('text-ja.txt', mode='a') as file2:
      file2.write(translation)
except FileNotFoundError as e:
  print('Check your file path silly!')

