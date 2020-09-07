class Animal:
  def __init__(self,name,species):
    self.species = species
    self.name = name

  def make_sound(self,sound):
    print(f"This animal says {sound}")
  
  def __repr__(self):
    return f"{self.name} is a {self.species}"
  

class Cat(Animal):
  def __init__(self,name,breed,favorite_toy):
    super().__init__(name, species="cat")
    self.breed = breed
    self.favorite_toy = favorite_toy

  

blue = Cat("blue","DSH","ball")

blue.make_sound("meow")

print(blue.species)