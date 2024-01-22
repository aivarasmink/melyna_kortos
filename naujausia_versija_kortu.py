import random
import time

# Define the unconverted deck with ranks and symbols
unconverted_deck = {'2❤️': 2, '3❤️': 3, '4❤️': 4, '5❤️': 5, '6❤️': 6, '7❤️': 7, '8❤️': 8, '9❤️': 9, '10❤️': 10, 'J❤️': 11,
                    'Q❤️': 12, 'K❤️': 13, 'A❤️': 15, '2♠️': 2, '3♠️': 3, '4♠️': 4, '5♠️': 5, '6♠️': 6, '7♠️': 7, '8♠️': 8,
                    '9♠️': 9, '10♠️': 10, 'J♠️': 11, 'Q♠️': 12, 'K♠️': 13, 'A♠️': 15, '2♦️': 2, '3♦️': 3, '4♦️': 4, '5♦️': 5,
                    '6♦️': 6, '7♦️': 7, '8♦️': 8, '9♦️': 9, '10♦️': 10, 'J♦️': 11, 'Q♦️': 12, 'K♦️': 13, 'A♦️': 15,
                    '2︎♣️': 2, '3♣️': 3, '4♣️': 4, '5♣️': 5, '6♣️': 6, '7♣️': 7, '8♣️': 8, '9♣️': 9, '10♣️': 10, 'J♣️': 11,
                    'Q♣️': 12, 'K♣️': 13, 'A♣️': 15}  # This is a dictionary of the unconverted deck

# Shuffle the deck
deckn = list(unconverted_deck)  # deckn is a list of tuples
random.shuffle(deckn)

# Split the deck between computer and player
computer_primary = deckn[1::2]  # computer_primary is a list of tuples [1::2] means every second element of the list
player_primary = deckn[0::2]  # player_primary is a list of tuples [0::2] means every first element of the list
random.shuffle(player_primary)
random.shuffle(computer_primary)

# Initialize discard piles for player and computer
player_secondary = []
computer_secondary = []

# Set the number of turns
turns = 5

# Initialize card indices and war-at-risk lists
play_card_index = 0
comp_card_index = 0
play_war_at_risk = []
comp_war_at_risk = []

# Main game loop
while turns > 0:
    print(f'\n\nRemaining Turns: {turns}')  # Display remaining turns
    try:  # Try means that if an error is thrown, the program will continue to run
        input("Press Enter to draw cards...")  # Pause for better visibility

        print(f"\nYour card: {player_primary[play_card_index]}")  # Display player's card
        print(f"Opponent's card: {computer_primary[comp_card_index]}")  # Display computer's card

        if unconverted_deck[player_primary[play_card_index]] > unconverted_deck[computer_primary[comp_card_index]]:
            # Player wins the round
            player_secondary.extend(
                [player_primary[play_card_index], computer_primary[comp_card_index]])  # Add cards to discard pile.
            player_primary.pop(play_card_index)  # Remove cards from player's deck
            computer_primary.pop(comp_card_index)  # Remove cards from computer's deck

            print(f"Player wins the round!\nPlayer discard: {player_secondary}\nCPU discard: {computer_secondary}")
        elif unconverted_deck[player_primary[play_card_index]] < unconverted_deck[computer_primary[comp_card_index]]:
            # Computer wins the round
            computer_secondary.extend(
                [player_primary[play_card_index], computer_primary[comp_card_index]])  # Add cards to discard pile.
            player_primary.pop(play_card_index)  # Remove cards from player's deck
