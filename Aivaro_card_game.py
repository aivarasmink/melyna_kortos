import random   # For random shuffle function
import time # For sleep function for better visibility. If you don't want to use this, you can remove the import time and the sleep function.

# Define the unconverted deck with ranks and symbols
unconverted_deck = {'2❤️': 2, '3❤️': 3, '4❤️': 4, '5❤️': 5, '6❤️': 6, '7❤️': 7, '8❤️': 8, '9❤️': 9, '10❤️': 10, 'J❤️': 11,
                    'Q❤️': 12, 'K❤️': 13, 'A❤️': 15, '2♠️': 2, '3♠️': 3, '4♠️': 4, '5♠️': 5, '6♠️': 6, '7♠️': 7, '8♠️': 8,
                    '9♠️': 9, '10♠️': 10, 'J♠️': 11, 'Q♠️': 12, 'K♠️': 13, 'A♠️': 15, '2♦️': 2, '3♦️': 3, '4♦️': 4, '5♦️': 5,
                    '6♦️': 6, '7♦️': 7, '8♦️': 8, '9♦️': 9, '10♦️': 10, 'J♦️': 11, 'Q♦️': 12, 'K♦️': 13, 'A♦️': 15,
                    '2︎♣️': 2, '3♣️': 3, '4♣️': 4, '5♣️': 5, '6♣️': 6, '7♣️': 7, '8♣️': 8, '9♣️': 9, '10♣️': 10, 'J♣️': 11,
                    'Q♣️': 12, 'K♣️': 13, 'A♣️': 15} # This is a dictionary of the unconverted deck

# Shuffle the deck
deckn = list(unconverted_deck)     # deckn is a list of tuples 
random.shuffle(deckn)

# Split the deck between computer and player
computer_primary = deckn[1::2] # computer_primary is a list of tuples [1::2] means every second element of the list
player_primary = deckn[0::2] # player_primary is a list of tuples [0::2] means every first element of the list 
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
    print(f'\n\nRemaining Turns: {turns}') # Display remaining turns
    try:            # Try means that if an error is thrown, the program will continue to run
        input("Press Enter to draw cards...") # Pause for better visibility

        print(f"\nYour card: {player_primary[play_card_index]}") # Display player's card
        print(f"Opponent's card: {computer_primary[comp_card_index]}") # Display computer's card

        if player_primary[play_card_index] > computer_primary[comp_card_index]: # Check if player's card is higher than computer's card
            # Player wins the round
            player_secondary.extend([player_primary[play_card_index], computer_primary[comp_card_index]]) # Add cards to discard pile. .extend() is a list concatenation function
            player_primary.pop(play_card_index) # Remove cards from player's deck
            computer_primary.pop(comp_card_index) # Remove cards from computer's deck

            print(f"Player wins the round!\nPlayer discard: {player_secondary}")    # Display discard pile
        elif player_primary[play_card_index] < computer_primary[comp_card_index]: # Check if player's card is lower than computer's card
            # Computer wins the round
            computer_secondary.extend([player_primary[play_card_index], computer_primary[comp_card_index]]) # Add cards to discard pile. .extend() means list concatenation function and list conectenation is done by adding the elements of one list to the end of another list
            player_primary.pop(play_card_index) # Remove cards from player's deck
            computer_primary.pop(comp_card_index)

            print(f"Computer wins the round!\nPlayer discard: {player_secondary}") # Display discard pile
        else:
            # It's a tie, going to war (optional)
            print("It's a tie! Going to war...")

    except IndexError:  
        # Handle index errors if cards run out
        print("Out of cards. Starting a new round...")
        player_primary.extend(player_secondary) # Add cards from discard pile to player's deck
        computer_primary.extend(computer_secondary)     # Add cards from discard pile to computer's deck
        random.shuffle(player_primary)
        random.shuffle(computer_primary)
        player_secondary = []
        computer_secondary = []
        turns -= 1

# Determine the winner of the game
if len(player_primary) > len(computer_primary):
    print("Player wins the game!")
else:
    print("Computer wins the game!")

