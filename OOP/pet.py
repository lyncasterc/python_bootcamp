class Pet:
  allowed = ['cat','dog','fish']
  def __init__(self, name, species):
    if species not in Pet.allowed:
      raise ValueError(f"You can not have a {species} as a pet")
    self.name = name
    self.species = species

    def set_species(self,species):
      if species not in Pet.allowed:
        raise ValueError(f"You can not have a {species} as a pet")


cat = Pet('Kitty', 'cat')
dog = Pet('Pupper', 'dog')