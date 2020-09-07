# classes can inhereit from base classes (aka parent classes). 
# ex - users on reddit all have the same base abilities, commenting, upvoting, email, etc. But someone users are mods and admins and each come with their own unique abilities.
# so you would have three classes for each type of user, but they all would inherit the base class.

class Animal:
  cool = True

  def make_sound(self,sound):
    print(f"This animal says {sound}")
  

class Cat(Animal):
  pass

# cat = Cat()

# cat.make_sound("meow")


# More Complex Example w/Properties ----------------------------

class Human:
  def __init__(self,first,last,age):
    self.first = first
    self.last = last
    if age >= 0:
      self._age = age
    else:
      self._age = 0
  
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self,value):
    if value >= 0:
      self._age = value
    else:
      self._age = 0
    
  @property
  def full_name(self):
    return f"{self.first} {self.last}"




jane = Human("Jane","Good", 4)

print(jane.age)

jane.age=20
print(jane.age)
print(jane.full_name)
