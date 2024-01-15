import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.sign = f"{self.suit} {self.rank}"
        self.weight = self.calculate_weight()

    def calculate_weight(self):
        rank_weights = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return rank_weights[self.rank]

    def convert_number_into_symbol(self):
        suit_symbols = {'Hearts': '♥', 'Diamonds': '♦', 'Spades': '♠', 'Clubs': '♣'}
        return suit_symbols.get(self.suit, '')

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        return [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def take_from_top(self):
        return self.cards.pop(0)

    def take_from_bottom(self):
        return self.cards.pop()

    def take_random(self):
        return self.cards.pop(random.randint(0, len(self.cards) - 1))

def play_war(player_deck, computer_deck):
    war_pile = []

    while True:
        for _ in range(4):  # Each player places one card face down and one card face up
            war_pile.append(player_deck.take_from_top())
            war_pile.append(computer_deck.take_from_top())

        player_face_up = player_deck.take_from_top()
        computer_face_up = computer_deck.take_from_top()

        print(f"\nWar! Player face-up: {player_face_up.sign} ({player_face_up.convert_number_into_symbol()})")
        print(f"Computer face-up: {computer_face_up.sign} ({computer_face_up.convert_number_into_symbol()})")

        war_pile.extend([player_face_up, computer_face_up])

        if player_face_up.weight > computer_face_up.weight:
            print("Player wins the war!")
            player_deck.cards.extend(war_pile)
            break
        elif computer_face_up.weight > player_face_up.weight:
            print("Computer wins the war!")
            computer_deck.cards.extend(war_pile)
            break
        else:
            print("War continues...")

def play_game():
    player_deck = Deck()
    computer_deck = Deck()
    player_deck.shuffle()
    computer_deck.shuffle()

    while player_deck.cards and computer_deck.cards:
        player_card = player_deck.take_from_top()
        computer_card = computer_deck.take_from_top()

        print(f"\nPlayer: {player_card.sign} ({player_card.convert_number_into_symbol()})")
        print(f"Computer: {computer_card.sign} ({computer_card.convert_number_into_symbol()})")

        if player_card.weight > computer_card.weight:
            print("Player wins the round!")
            player_deck.cards.extend([player_card, computer_card])
        elif computer_card.weight > player_card.weight:
            print("Computer wins the round!")
            computer_deck.cards.extend([player_card, computer_card])
        else:
            print("It's a tie! Going to war...")
            play_war(player_deck, computer_deck)

    if not player_deck.cards:
        print("Computer wins the game!")
    else:
        print("Player wins the game!")

# Example Usage:
if __name__ == "__main__":
    print("Welcome to the War card game!")

    play_game()
