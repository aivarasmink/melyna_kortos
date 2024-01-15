import random

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'A', 'Q']
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

class Card():
    def __init__(self, suit, rank): # this is a function that creates the card
        self.suit = suit 
        self.rank = rank    

    def convert_number_into_symbol(self):   # this is a function that converts the number into the symbol
        if self.suit == 'Hearts':
            return "\u2665" # this is a function that converts the number into the symbol
        elif self.suit == 'Diamonds':
            return "\u2666"
        elif self.suit == 'Spades':
            return "\u2660"
        elif self.suit == 'Clubs':
            return "\u2663"

    def compare_card_rank(self, computer, player): # this is a function that compares the rank of the cards
        print(f"Computer: {computer.rank} {computer.convert_number_into_symbol()}") # this is a function that compares the rank of the cards
        print(f"Player: {player.rank} {player.convert_number_into_symbol()}") # this is a function that compares the rank of the cards

        if computer.rank > player.rank:
            print("You lost")
        elif player.rank > computer.rank:
            print("You won")
        elif player.rank == computer.rank:  # this is a function that compares the rank of the cards
            print("Draw, flip again")

def create_deck():
    ranks = list(range(2, 15)) 
    deck = [Card(suit, rank) for suit in suits for rank in ranks] # this is a function that creates the deck
    random.shuffle(deck) 
    return deck

def take_from_top(deck): # this is a function that takes a card from the top of the deck
    return deck.pop(0)

def take_from_bottom(deck): # this is a function that takes a card from the bottom of the deck
    return deck.pop()

def take_random(deck):
    return deck.pop(random.randint(0, len(deck) - 1)) # this is a function that takes a random card from the deck

print("Welcome to the best card game! War!")

while True:
    deck = create_deck()

    choice = input("Do you want to take a card from the top or bottom? (top/bottom): ").lower()

    if choice == 'top':
        player_card = take_from_top(deck)
        computer_card = take_random(deck)
    elif choice == 'bottom':
        player_card = take_from_bottom(deck)
        computer_card = take_random(deck)
    else:
        print("Invalid choice. Please enter 'top' or 'bottom'.")
        continue

    compare = Card('', '') # this is a function that compares the rank of the cards
    compare.compare_card_rank(computer_card, player_card)

    play_again = input("Do you want to play again? (yes/no): ").lower() # this is a function that compares the rank of the cards
    if play_again != 'yes':
        break


    



#Kort kaladė
#Korta: objektas
#rank (2-9, T, J, Q, K, A)
#suit (spades, clubs, hearts, diamonds)
#sign (suit + rank)
#weight
#Kortų kaladė
#cards - sąrašas kortų
#shuffle
#take from top
#take from bottom
#take random
#mastom apie žaidimą