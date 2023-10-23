import random
from playing_card import PlayingCard
from hand import Hand

vals = [*(n for n in range(2, 10)), 'J', 'Q', 'K', 'A']
suits = ['spade', 'heart', 'diamond', 'club']
deck = [PlayingCard(val, suit) for val in vals for suit in suits]

hand = Hand()

for n in range(5):
  card = random.choice(deck)
  deck.remove(card)
  hand.add_card(card)

print(hand)