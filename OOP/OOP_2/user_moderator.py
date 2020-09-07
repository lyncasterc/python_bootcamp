class User:
  active_users = 0 #class attribute

  @classmethod
  def display_active_users(cls):
    return f"{cls.active_users} online right now"

  @classmethod
  def from_string(cls,data_str):
    first, last, age = data_str.split(',')
    age = int(age)
    return cls(first, last, age)

  def __init__(self,first,last,age):
    self.first = first
    self.last = last
    self.age = age
    User.active_users += 1
  
  def __repr__(self):
    return f"{self.first} {self.last}"
  
  def logout(self):
    User.active_users -= 1
    return f"{self.first} has logged out"

  def full_name(self):
    return f"{self.first} {self.last}"

  def initials(self):
    return f"{self.first[0]}.{self.last[0]}."


class Moderator(User):
  def __init__(self,first,last,age,community):
    super().__init__(first,last,age)
    self.community = community
  
  def remove_post(self):
    pass


jasmine = Moderator("Jaz","Bazz", 20,"Piano")