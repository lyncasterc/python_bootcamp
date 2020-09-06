import random

class Card:

  def __init__(self,value,suit):

    self.suit = suit
    self.value = value
  
  def __repr__(self):
    return f"{self.value} of {self.suit}"

class Deck:
  def __init__(self,cards=None):
    suits = ["Hearts","Diamonds","Clubs","Spades"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]  
    
    self.cards = cards or [Card(value, suit) for value in values for suit in suits]



# need to create instance method count to see how many cards left



# card1 = Card("A", "Hearts")
# print(card1.suit)
# print(card1)

deck1 = Deck()

print(deck1.cards)