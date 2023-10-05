class PlayingCard:
  def __init__(self, value: str, suit: str):
    self.value = value
    self.suit = suit

  def getValue(self):
    return self.value

  def getSuit(self):
    return self.suit

  def setValue(self, value):
    self.value = value

  def setSuit(self, suit):
    self.suit = suit

  def print_val(self):
    print(f'This card is the {self.value} of {self.suit}s')

  def __add__(self, other):
    return self.getValue() + other.getValue() 

  def __lt__(self, other):
    return self.getValue() < other.getValue()

  def __gt__(self, other):
    return self.getValue() > other.getValue()

  def __eq__(self, other):
    return self.getValue() == other.getValue() and self.getSuit() == other.getSuit()

  def __str__(self):
    self.print_val()