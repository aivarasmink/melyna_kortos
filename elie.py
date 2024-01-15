import random

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def convert_number_into_symbol(self):
        if self.suit == '1':
            return "\u2663"
        elif self.suit == '2':
            return "\u2665"
        elif self.suit == '3':
            return "\u2666"
        elif self.suit == '4':
            return "\u2660"

    def compare_card_rank(self, computer, player):
        print(f"Computer: {self.convert_number_into_symbol()} {computer}")
        print(f"Player: {self.convert_number_into_symbol()} {player}")

        if computer > player:
            print("You lost")
        elif player > computer:
            print("You won")
        elif player == computer:
            print("Draw, flip again")

def create_deck():
    suits = ['1', '2', '3', '4']
    ranks = list(range(1, 14))
    deck = [Card(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

while True:
    deck = create_deck()

    player_card = deck.pop()
    computer_card = deck.pop()

    compare = Card('', '')
    compare.compare_card_rank(computer_card.rank, player_card.rank)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
