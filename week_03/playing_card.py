# playing card
# Andy Mina
# CSCI 77800 Fall 2023
class PlayingCard:
  def __init__(self, value: str, suit: str):
    self.value = value
    self.suit = suit
    self.symbolMap = {
      'spade': '♠',
      'heart': '♥',
      'club': '♣',
      'diamond': '◆'
    }

  def getValue(self):
    return self.value

  def getSuit(self):
    return self.suit

  def setValue(self, value):
    self.value = value

  def setSuit(self, suit):
    self.suit = suit

  def print_val(self):
    print(f'This card is the {self.value} of {self.symbolMap[self.suit]}s')

  def __add__(self, other):
    return self.getValue() + other.getValue() 

  def __lt__(self, other):
    return self.getValue() < other.getValue()

  def __gt__(self, other):
    return self.getValue() > other.getValue()

  def __eq__(self, other):
    return self.getValue() == other.getValue()

  def __str__(self):
    return f'This card is the {self.value} of {self.symbolMap[self.suit]}s'

  def __hash__(self):
    return hash((self.value, self.suit))