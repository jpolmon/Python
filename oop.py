class PlayerCharacter:
  #Class Object Attribute
  membership = True
  
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def shout(self):
    print(f'My name is {self.name}!')

  @classmethod
  def adding_things(cls, num1, num2):
    return num1 + num2

  @staticmethod
  def adding_things2(num1, num2):
    return num1 + num2

player1 = PlayerCharacter('JP', 28)

print(player1)
print(player1.name)
print(player1.age)

player1.shout()

print(player1.adding_things(2,3))
print(PlayerCharacter.adding_things(2,3))

# You can call class methods without instantiating the class itself, or use them to create an instance with cls. You use static method when you don't care about the characteristics of the class.

# Inheritance - allowing a class to have access to properties/methods of the parent class.

class User():
  def sign_in(self):
    print('logged in')

class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'attacking with power of {self.power}')

class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
print(wizard1.attack())
print(archer1.attack())

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object)) # all classes inherit from the base object class

# Example exercise of using inheritance

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Tom(Cat):
  def sing(self, sounds):
    return f'{sounds}'
      
#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon('Simon', 22), Sally('Sally', 19), Tom('Tom', 21)]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
for pet in my_pets.animals:
  print(pet.walk())

# Using super() - Lets you access variables that are established in the parent class.

class User():
  def __init__(self, email):
    self.email = email
  
  def sign_in(self):
    print('logged in')

class Wizard(User):
  def __init__(self, name, power, email):
    super().__init__(email)
    #User.__init__(self, email)
    self.name = name
    self.power = power

  def attack(self):
    print(f'attacking with power of {self.power}')

class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(wizard1.email)
# using dir() lets you see what methods you have access to in a given class object.
print(dir(wizard1))

# Dunder Methods - You generally should not modify them.

class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
      'name': 'Yoyo',
      'has_pets': False
    }

  def __str__(self):        # You can modify the dunder methods locally
    return f'{self.color}'

  def __len__(self):
    return 5

  def __del__(self):
    print('deleted!')

  def __call__(self):
    return('yess??')

  def __getitem__(self, i):
    return self.my_dict[i]

action_figure = Toy('Red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['has_pets'])
del action_figure

# Exercise - You can get all of the properties of a list by using inheritance

class SuperList(list):
  def __len__(self):
    return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])

# Multiple Inheritance - Bringing in variables and methods from multiple classes into one. 

class User():  
  def sign_in(self):
    print('logged in')

class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'attacking with power of {self.power}')

class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'attacking with arrows: arrows left - {self.num_arrows}')

  def check_arrows(self):
    print(f'{self.num_arrows} remaining')

  def run(self):
    print('ran really fast')

class HybridBorg(Wizard, Archer):
  def __init__(self, name, power, arrows):
    Archer.__init__(self, name, arrows)
    Wizard.__init__(self, name, power)

hybrid1 = HybridBorg('Borg', 50, 100)
print(hybrid1.run())
print(hybrid1.check_arrows())
print(hybrid1.attack())
print(hybrid1.sign_in())