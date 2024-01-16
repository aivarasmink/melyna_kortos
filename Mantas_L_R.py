import random
from itertools import product
from time import sleep

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", 
         "Spades", "Clubs"] 


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.weight = self.calculate_weight()

    def calculate_weight(self):
        if isinstance(self.rank, int):
            return self.rank
        elif self.rank == 'J':
            return 11
        elif self.rank == 'K':
            return 13
        elif self.rank == 'A':
            return 14
        else:
            return 12

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

        if computer.weight > player.weight:
            print("You lost")
        elif player.weight > computer.weight:
            print("You won")
        elif player.weight == computer.weight:
            print("Draw, flip again")


def create_deck():
    deck = [Card(suit, rank) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def take_from_top(deck):
    return deck.pop(0)

def take_from_bottom(deck):
    return deck.pop()

def take_random(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

def show_deck():
    suits = ["\u2663", "\u2665", "\u2666", "\u2660"] 
    print("\n--- Whole deck of card ---\n")
    for rank in ranks: 
        for suit in suits:
            print(f'{rank} of {suit}'.ljust(10), end='')
        print()

def shuffle_deck():
    suits = ["\u2663", "\u2665", "\u2666", "\u2660"] 
    print("\n--- Shuffled deck ---\n")
    deck = list(product(ranks, suits)) 
    random.shuffle(deck)

    cards_per_row = 13  # Adjust the number of cards per row as needed
    
    for i, card in enumerate(deck, start=1):
        print(f'{card[0]} {card[1]}', end=' ')
        
        if i % cards_per_row == 0:
            print()  # Move to the next line after printing the specified number of cards per row   

print("Welcome to the best card game!")

def main():
    while True:
        deck = create_deck()

        sleep(1)  # Adding a delay for better visibility
        print('--- Choose your fate: ---')
        print('--- 0: Exit program ---')
        print('--- 1: Show whole deck ---')
        print('--- 2: Show whole deck shuffled ---')
        print('--- 3: Play War Game ---')
        choice = input('Choose: ')
        if choice == "0":
            print("Program closed. bye!")
            break
        elif choice == "1":
            show_deck()
        elif choice == "2":
            shuffle_deck()
        elif choice == "3":
            choice = input("Take a card from the top, bottom or random? (top/bottom/random): ").lower()
            if choice == 'top':
                player_card = take_from_top(deck)
                computer_card = take_random(deck)
            elif choice == 'bottom':
                player_card = take_from_bottom(deck)
                computer_card = take_random(deck)
            elif choice == 'random':
                player_card = take_random(deck)
                computer_card = take_random(deck)
            else:
                print("Invalid choice. Please enter 'top', 'bottom' or 'random'.")
                continue
            compare = Card('', '')
            compare.compare_card_rank(computer_card, player_card)
            play_again = input("Return to main menu? (yes/no): ").lower()
            if play_again == 'yes':
                continue
            elif play_again == 'no':
                break 
        else:
            print("Bad input! Choose a number between 0-3!")
            continue

main()