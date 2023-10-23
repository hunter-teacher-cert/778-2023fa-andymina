# deck
# Andy Mina
# CSCI 77800 Fall 2023
import random

class Hand:
  def __init__(self):
    self.cards = []

  def add_card(self, card):
    self.cards.append(card)

  def remove_random(self):
    idx = random.randrange(len(self.cards))
    card = self.cards[idx]
    self.cards.remove(card)

  def has_match(self, other):
    """
    Instructions for this were unclear. Functions prefixed with has usually
    return a boolean indicating some status. The description on the assignment
    says: returns 0, 2, 3, 4, dependong on the number of cards that match.

    There's no guarantee that the other hand would have at least 4 cards 
    and also why is 1 omitted? The following part of the assignment is to create
    a hand of 5 card so the missing 1 seem intentional?
    """
    other = set(other.cards)
    hand = set(self.cards)
    return len(list(hand & other)) > 1
  
  def __str__(self):
    res = ""
    for card in self.cards:
      res += str(card) + "\n"
    
    return res
