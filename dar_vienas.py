import random
import time

# Define the unconverted deck with ranks and symbols
unconverted_deck = {'2❤️': 2, '3❤️': 3, '4❤️': 4, '5❤️': 5, '6❤️': 6, '7❤️': 7, '8❤️': 8, '9❤️': 9, '10❤️': 10, 'J❤️': 11,
                    'Q❤️': 12, 'K❤️': 13, 'A❤️': 15, '2♠️': 2, '3♠️': 3, '4♠️': 4, '5♠️': 5, '6♠️': 6, '7♠️': 7, '8♠️': 8,
                    '9♠️': 9, '10♠️': 10, 'J♠️': 11, 'Q♠️': 12, 'K♠️': 13, 'A♠️': 15, '2♦️': 2, '3♦️': 3, '4♦️': 4, '5♦️': 5,
                    '6♦️': 6, '7♦️': 7, '8♦️': 8, '9♦️': 9, '10♦️': 10, 'J♦️': 11, 'Q♦️': 12, 'K♦️': 13, 'A♦️': 15,
                    '2︎♣️': 2, '3♣️': 3, '4♣️': 4, '5♣️': 5, '6♣️': 6, '7♣️': 7, '8♣️': 8, '9♣️': 9, '10♣️': 10, 'J♣️': 11,
                    'Q♣️': 12, 'K♣️': 13, 'A♣️': 15}

# Shuffle the deck
oedokn = list(unconverted_deck)
random.shuffle(oedokn)

# Split the deck between computer and player
computer_primary = oedokn[1::2]
player_primary = oedokn[0::2]
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
    print(f'\n\nRemaining Turns: {turns}')
    try:
        input("Press Enter to draw cards...")

        print(f"\nYour card: {player_primary[play_card_index]}")
        print(f"Opponent's card: {computer_primary[comp_card_index]}")

        if player_primary[play_card_index] > computer_primary[comp_card_index]:
            # Player wins the round
            player_secondary.extend([player_primary[play_card_index], computer_primary[comp_card_index]])
            player_primary.pop(play_card_index)
            computer_primary.pop(comp_card_index)

            print(f"Player wins the round!\nPlayer discard: {player_secondary}")
        elif player_primary[play_card_index] < computer_primary[comp_card_index]:
            # Computer wins the round
            computer_secondary.extend([player_primary[play_card_index], computer_primary[comp_card_index]])
            player_primary.pop(play_card_index)
            computer_primary.pop(comp_card_index)

            print(f"Computer wins the round!\nPlayer discard: {player_secondary}")
        else:
            # It's a tie, going to war (optional)
            print("It's a tie! Going to war...")

    except IndexError:
        # Handle index errors if cards run out
        print("Out of cards. Starting a new round...")
        player_primary.extend(player_secondary)
        computer_primary.extend(computer_secondary)
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

