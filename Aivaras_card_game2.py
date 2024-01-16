import random
import time

def initialize_deck():
    unconverted_deck = {'2❤️': 2, '3❤️': 3, '4❤️': 4, '5❤️': 5, '6❤️': 6, '7❤️': 7, '8❤️': 8, '9❤️': 9, '10❤️': 10, 'J❤️': 11,
                        'Q❤️': 12, 'K❤️': 13, 'A❤️': 15, '2♠️': 2, '3♠️': 3, '4♠️': 4, '5♠️': 5, '6♠️': 6, '7♠️': 7, '8♠️': 8,
                        '9♠️': 9, '10♠️': 10, 'J♠️': 11, 'Q♠️': 12, 'K♠️': 13, 'A♠️': 15, '2♦️': 2, '3♦️': 3, '4♦️': 4, '5♦️': 5,
                        '6♦️': 6, '7♦️': 7, '8♦️': 8, '9♦️': 9, '10♦️': 10, 'J♦️': 11, 'Q♦️': 12, 'K♦️': 13, 'A♦️': 15,
                        '2︎♣️': 2, '3♣️': 3, '4♣️': 4, '5♣️': 5, '6♣️': 6, '7♣️': 7, '8♣️': 8, '9♣️': 9, '10♣️': 10, 'J♣️': 11,
                        'Q♣️': 12, 'K♣️': 13, 'A♣️': 15}
    deck = list(unconverted_deck)
    random.shuffle(deck)
    return deck

def play_card_game(deck):
    player_deck = deck[:26]
    computer_deck = deck[26:]

    player_secondary = []
    computer_secondary = []

    turns = 5

    while turns > 0: 
        print(f'\n\nRemaining Turns: {turns}')
        try:
            input("Press Enter to draw cards...")
            
            player_card = player_deck.pop(0)
            computer_card = computer_deck.pop(0)

            print(f"\nYour card: {player_card}")
            print(f"Opponent's card: {computer_card}")

            if player_card > computer_card:
                player_secondary.extend([player_card, computer_card])
                player_deck.pop(0)
                computer_deck.pop(0)
                print(f"Player wins the round!\nPlayer discard: {player_secondary}")
            elif player_card < computer_card:
                computer_secondary.extend([player_card, computer_card])
                player_deck.pop(0)
                computer_deck.pop(0)
                print(f"Computer wins the round!\nPlayer discard: {player_secondary}")
            else:
                print("It's a tie! Going to war...")

                war_cards_to_place = 3
                if len(player_deck) < war_cards_to_place or len(computer_deck) < war_cards_to_place:
                    print("Not enough cards for war. Resolving as a tie.")
                else:
                    play_war_at_risk = player_deck[:war_cards_to_place]
                    comp_war_at_risk = computer_deck[:war_cards_to_place]

                    player_deck = player_deck[war_cards_to_place:]
                    computer_deck = computer_deck[war_cards_to_place:]

                    print(f"\nWar! Player's cards at risk: {play_war_at_risk}")
                    print(f"War! Computer's cards at risk: {comp_war_at_risk}")

                    if max(play_war_at_risk) > max(comp_war_at_risk):
                        player_secondary.extend(play_war_at_risk + comp_war_at_risk)
                        print("Player wins the war!")
                    elif max(play_war_at_risk) < max(comp_war_at_risk):
                        computer_secondary.extend(play_war_at_risk + comp_war_at_risk)
                        print("Computer wins the war!")
                    else:
                        player_deck.extend(play_war_at_risk)
                        computer_deck.extend(comp_war_at_risk)
                        print("It's a tie in the war!")

        except IndexError:  
            print("Out of cards. Starting a new round...")
            player_deck.extend(player_secondary)
            computer_deck.extend(computer_secondary)
            random.shuffle(player_deck)
            random.shuffle(computer_deck)
            player_secondary = [] 
            computer_secondary = []
            turns -= 1 

    if len(player_deck) > len(computer_deck):
        print("Player wins the game!")
    elif len(player_deck) < len(computer_deck):
        print("Computer wins the game!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    deck = initialize_deck()
    play_card_game(deck)
