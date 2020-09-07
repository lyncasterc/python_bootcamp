import random as rand

class Card:

  def __init__(self,value,suit):

    self.suit = suit
    self.value = value
  
  def __repr__(self):
    return f"{self.value} of {self.suit}"

class Deck:
  def __init__(self):
    suits = ["Hearts","Diamonds","Clubs","Spades"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]  
    
    self.cards = [Card(value, suit) for value in values for suit in suits]
  
  def __repr__(self):
    return f"Deck of {self.count()} cards"

  def count(self):
    return len(self.cards)
  
  def _deal(self,num):
    i = 0
    diff = 0
    removed_cards = []
    if self.count() > num or self.count() == num:
      while i < num:
        a = self.cards.pop()
        removed_cards.append(a)
        i+=1
    elif self.count() < num:
      diff = num - self.count()
      num -= diff
      while i < num:
        a = self.cards.pop()
        removed_cards.append(a)
        i+=1
    if self.count() == 0:
      raise ValueError("All cards have been dealt")
    
    return removed_cards
  
  def shuffle(self):
    if self.count() < 52:
      raise ValueError("Only full decks can be shuffled.")
    else:
      return rand.shuffle(self.cards)
  
  def deal_card(self):
    return self._deal(1)[0]
    

  def deal_hand(self, num):
    return self._deal(num)
    



  
  







deck1 = Deck()
print(deck1.deal_card())
print(deck1.deal_hand(5))