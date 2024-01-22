# Main game loop
while turns > 0 and player_primary and computer_primary:  # Check if there are turns left and both players have cards
    print(f'\n\nRemaining Turns: {turns}')  # Display remaining turns
    try:
        input("Press Enter to draw cards...")  # Pause for better visibility

        print(f"\nYour card: {player_primary[play_card_index]}")  # Display player's card
        print(f"Opponent's card: {computer_primary[comp_card_index]}")  # Display computer's card

        if unconverted_deck[player_primary[play_card_index]] > unconverted_deck[computer_primary[comp_card_index]]:
            # Player wins the round
            player_secondary.extend([player_primary[play_card_index], computer_primary[comp_card_index]])
            player_primary.pop(play_card_index)
            computer_primary.pop(comp_card_index)
            print(f"Player wins the round!\nPlayer discard: {player_secondary}\nCPU discard: {computer_secondary}")
        elif unconverted_deck[player_primary[play_card_index]] < unconverted_deck[computer_primary[comp_card_index]]:
            # Computer wins the round
            computer_secondary.extend([player_primary[play_card_index], computer_primary[comp_card_index]])
            player_primary.pop(play_card_index)
            computer_primary.pop(comp_card_index)
            print(f"Computer wins the round!\nPlayer discard: {player_secondary}\n CPU discard: {computer_secondary}")
        else:
            # It's a tie, going to war
            print("It's a tie! Going to war...")

            # Add logic for war (you can adjust the number of cards placed in the war)
            war_cards_to_place = 3
            if len(player_primary) < war_cards_to_place or len(computer_primary) < war_cards_to_place:
                print("Not enough cards for war. Resolving as a tie.")
            else:
                play_war_at_risk.extend(player_primary[:war_cards_to_place])
                comp_war_at_risk.extend(computer_primary[:war_cards_to_place])

                player_primary = player_primary[war_cards_to_place:]
                computer_primary = computer_primary[war_cards_to_place:]

                print(f"\nWar! Player's cards at risk: {play_war_at_risk}")
                print(f"War! Computer's cards at risk: {comp_war_at_risk}")

                if unconverted_deck[sum(play_war_at_risk)] > unconverted_deck[sum(comp_war_at_risk)]:
                    player_secondary.extend(play_war_at_risk + comp_war_at_risk)
                    print("Player wins the war!")
                elif unconverted_deck[sum(play_war_at_risk)] < unconverted_deck[sum(comp_war_at_risk)]:
                    computer_secondary.extend(play_war_at_risk + comp_war_at_risk)
                    print("Computer wins the war!")
                else:
                    player_primary.extend(play_war_at_risk)
                    computer_primary.extend(comp_war_at_risk)
                    print("It's a tie in the war!")

            play_war_at_risk = []
            comp_war_at_risk = []

        turns -= 1

    except IndexError:
        print("Out of cards. Ending the game...")

# Determine the winner of the game
if len(player_primary) > len(computer_primary):
    print("Player wins the game!")
elif len(player_primary) < len(computer_primary):
    print("Computer wins the game!")
else:
    print("It's a tie!")
