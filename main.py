class PlayerCharacter:
  #Class Object Attribute
  membership = True
  
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def run(self):
    print('run')

player1 = PlayerCharacter('JP', 28)

print(player1)
print(player1.name)
print(player1.age)

player1.run()