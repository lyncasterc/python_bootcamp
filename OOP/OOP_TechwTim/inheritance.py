class Pet:
  def __init__(self,name,age,breed):
    self.name = name
    self.age = age
    self.breed = breed


class Cat(Pet): 
  def speak(self):
    print("Meow")

class Dog(Pet):
  def speak(self):
    print("Bark")

