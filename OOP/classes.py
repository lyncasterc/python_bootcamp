class User:
  active_users = 0 #class attribute
  def __init__(self,first,last,age):
    self.first = first
    self.last = last
    self.age = age
    User.active_users += 1
  
  def logout(self):
    User.active_users -= 1
    return f"{self.first} has logged out"

  def full_name(self):
    return f"{self.first} {self.last}"

  def initials(self):
    return f"{self.first[0]}.{self.last[0]}."



# print(user1.full_name(), user1.initials())

user1 = User("Joe","Bosch", 32)
user2 = User("Blanca", "La Paz", 22)
print(User.active_users)
print(user2.logout())
print(User.active_users)
