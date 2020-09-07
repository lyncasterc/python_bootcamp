class Character:
  def __init__(self,name,hp,level):
    self.name = name
    self.hp = hp
    self.level = level

class NPC(Character):
  def __init__(self,name,hp,level,speech):
    super().__init__(name,hp,level)
    self.speech = speech

  def speak(self):
    print(f"{self.speak}")


villager = NPC("bob",100,12)


