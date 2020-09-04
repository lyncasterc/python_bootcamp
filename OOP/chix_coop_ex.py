class Chicken:
  total_eggs = 0
  def __init__(self, name,species,eggs=0):
    self.name = name
    self.species = species
    self.eggs = eggs

  def lay_eggs(self,num):
    Chicken.total_eggs += num
    self.eggs += num
    return self.eggs
  

chix_1 = Chicken("billy", "cock")
chix_2 = Chicken("bob", "cock")


chix_1.lay_eggs(12)
chix_1.lay_eggs(10)

chix_2.lay_eggs(5)





print(Chicken.total_eggs)