from PIL import Image

class Card:

    spade = "spade"
    heard = "heart"
    diamond = "diamond"
    clube = "club"

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    def image(self):
        return 'War_card_Game/card_deck_1' + self.suit + '-' + self.rank + '.png'