import random

class Deck:
  def __init__(self):
    self.cards = []

  def add_card(self, card):
    self.cards.append(card)

  def remove_random(self):
    idx = random.randrange(len(self.cards))
    card = self.cards[idx]
    self.cards.remove(card)

  def has_match(self, hand):
    hand_set = set(hand)
    