import random
import time

class Card():
    def __init__(self, suit, rank):
        self.suit = suit 
        self.rank = rank

    def convert_number_into_symbol(self):
        if self.suit == 'Hearts':
            return "\u2665"
        elif self.suit == 'Diamonds':
            return "\u2666"
        elif self.suit == 'Spades':
            return "\u2660"
        elif self.suit == 'Clubs':
            return "\u2663"

    def compare_card_rank(self, computer, player):
        print(f"Computer: {computer.rank} {computer.convert_number_into_symbol()}")
        print(f"Player: {player.rank} {player.convert_number_into_symbol()}")

        if computer.rank > player.rank:
            print("You lost")
            return 'computer'
        elif player.rank > computer.rank:
            print("You won")
            return 'player'
        else:
            print("Draw! It's War!")
            return 'war'

def create_deck():
    ranks = list(range(2, 15)) 
    deck = [Card(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def take_from_top(deck):
    return deck.pop(0)

def take_from_bottom(deck):
    return deck.pop()

def take_random(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

def resolve_war(player_pile, computer_pile):
    war_result = None

    while len(player_pile) >= 4 and len(computer_pile) >= 4:
        # Each player places one card face down
        play_war_at_risk.extend([player_pile.pop(0) for _ in range(3)])
        comp_war_at_risk.extend([computer_pile.pop(0) for _ in range(3)])

        # Each player turns up one card face up
        player_up_card = player_pile.pop(0)
        comp_up_card = computer_pile.pop(0)

        print(f"\nWar! Player's face-up card: {player_up_card.rank} {player_up_card.convert_number_into_symbol()}")
        print(f"War! Computer's face-up card: {comp_up_card.rank} {comp_up_card.convert_number_into_symbol()}")

        # Compare face-up cards
        if player_up_card.rank > comp_up_card.rank:
            print("Player wins the War!")
            war_result = 'player'
        elif player_up_card.rank < comp_up_card.rank:
            print("Computer wins the War!")
            war_result = 'computer'
        else:
            print("It's still a tie! War continues...")

    return war_result

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

print("Welcome to the best card game! War!")

while True:
    deck = create_deck()

    # Initialize player and computer piles
    player_primary = deck[0::2]
    computer_primary = deck[1::2]

    # Initialize discard piles for player and computer
    player_secondary = []
    computer_secondary = []

    turns = 5

    while turns > 0:
        print(f'\n\nRemaining Turns: {turns}')
        input("Press Enter to draw cards...")

        player_card = take_from_top(player_primary)
        computer_card = take_random(computer_primary)

        print(f"\nYour card: {player_card.rank} {player_card.convert_number_into_symbol()}")
        print(f"Computer's card: {computer_card.rank} {computer_card.convert_number_into_symbol()}")

        compare = Card('', '')
        result = compare.compare_card_rank(computer_card, player_card)

        if result == 'computer':
            computer_secondary.extend([player_card, computer_card])
        elif result == 'player':
            player_secondary.extend([player_card, computer_card])
        else:
            # It's a tie, go to war
            play_war_at_risk = [player_card]
            comp_war_at_risk = [computer_card]

            war_winner = resolve_war(player_primary, computer_primary)

            if war_winner == 'player':
                player_secondary.extend(play_war_at_risk + comp_war_at_risk)
            elif war_winner == 'computer':
                computer_secondary.extend(play_war_at_risk + comp_war_at_risk)
            else:
                # War is unresolved
                print("War is unresolved. Continuing to the next turn...")

        turns -= 1

    # Determine the winner of the game
    if len(player_primary) + len(player_secondary) > len(computer_primary) + len(computer_secondary):
        print("Player wins the game!")
    else:
        print("Computer wins the game!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

