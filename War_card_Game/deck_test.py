from card import Card
from deck import Deck
import os

a = Deck()

a.add('A', 'Hearts')
a.names()
a.remove()
a.look()
a.names()

folder = len(os.listdir('War_card_Game/card_deck_1'))
print(folder)