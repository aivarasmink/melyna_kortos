if unconverted_deck[player_primary[play_card_index]] > unconverted_deck[computer_primary[comp_card_index]]:
    # Player wins the round
    player_secondary.extend([player_primary[play_card_index], computer_primary[comp_card_index]])  # Add cards to discard pile.
    player_primary.pop(play_card_index)  # Remove cards from player's deck
    computer_primary.pop(comp_card_index)  # Remove cards from computer's deck

    print(f"Player wins the round!\nPlayer discard: {player_secondary}\nCPU discard: {computer_secondary}")
elif unconverted_deck[player_primary[play_card_index]] < unconverted_deck[computer_primary[comp_card_index]]:
    # Computer wins the round
    computer_secondary.extend([player_primary[play_card_index], computer_primary[comp_card_index]])  # Add cards to discard pile.
    player_primary.pop(play_card_index)  # Remove cards from player's deck
    computer_primary.pop(comp_card_index)  # Remove cards from computer's deck

    print(f"Computer wins the round!\nPlayer discard: {player_secondary}\n CPU discard: {computer_secondary}")
else:
    # It's a tie, going to war
    print("It's a tie! Going to war...")

    # Add logic for war (you can adjust the number of cards placed in the war)
    war_cards_to_place = 3
    if len(player_primary) < war_cards_to_place or len(computer_primary) < war_cards_to_place:
        print("Not enough cards for war. Resolving as a tie.")
        # Handle as a tie (optional)
    else:
        play_war_at_risk.extend(player_primary[:war_cards_to_place])
        comp_war_at_risk.extend(computer_primary[:war_cards_to_place])

        # Remove war cards from the players' decks
        player_primary = player_primary[war_cards_to_place:]
        computer_primary = computer_primary[war_cards_to_place:]

        # Display the cards placed in the war
        print(f"\nWar! Player's cards at risk: {play_war_at_risk}")
        print(f"War! Computer's cards at risk: {comp_war_at_risk}")

        # Resolve the war
        if unconverted_deck[sum(play_war_at_risk)] > unconverted_deck[sum(comp_war_at_risk)]:
            # Player wins the war
            player_secondary.extend(play_war_at_risk + comp_war_at_risk)
            print("Player wins the war!")
        elif unconverted_deck[sum(play_war_at_risk)] < unconverted_deck[sum(comp_war_at_risk)]:
            # Computer wins the war
            computer_secondary.extend(play_war_at_risk + comp_war_at_risk)
            print("Computer wins the war!")
        else:
            # It's a tie in the war, add the cards back to the players' decks
            player_primary.extend(play_war_at_risk)
            computer_primary.extend(comp_war_at_risk)
            print("It's a tie in the war!")

    # Clear the war-at-risk lists
    play_war_at_risk = []
    comp_war_at_risk = []
