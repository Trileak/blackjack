import random
import time

def draw_card(deck):
    return random.choice(deck)  # Randomly select a card without removing it

# Create all cards and their Blackjack values using a matrix
cards = [
    ["2 ♥", 2], ["3 ♥", 3], ["4 ♥", 4], ["5 ♥", 5], ["6 ♥", 6], ["7 ♥", 7], ["8 ♥", 8], ["9 ♥", 9], ["10 ♥", 10], ["J ♥", 10], ["Q ♥", 10], ["K ♥", 10], ["A ♥", 1],
    ["2 ♦", 2], ["3 ♦", 3], ["4 ♦", 4], ["5 ♦", 5], ["6 ♦", 6], ["7 ♦", 7], ["8 ♦", 8], ["9 ♦", 9], ["10 ♦", 10], ["J ♦", 10], ["Q ♦", 10], ["K ♦", 10], ["A ♦", 1],
    ["2 ♣", 2], ["3 ♣", 3], ["4 ♣", 4], ["5 ♣", 5], ["6 ♣", 6], ["7 ♣", 7], ["8 ♣", 8], ["9 ♣", 9], ["10 ♣", 10], ["J ♣", 10], ["Q ♣", 10], ["K ♣", 10], ["A ♣", 1],
    ["2 ♠", 2], ["3 ♠", 3], ["4 ♠", 4], ["5 ♠", 5], ["6 ♠", 6], ["7 ♠", 7], ["8 ♠", 8], ["9 ♠", 9], ["10 ♠", 10], ["J ♠", 10], ["Q ♠", 10], ["K ♠", 10], ["A ♠", 1]
]

chips = 1500  # Starting chips

def learn():
    while True:
        learned = input("Do you know how to play blackjack? [Y/N] ").strip().lower()
        if learned not in ["y", "n"]:
            print("Type Y or N")
        else:
            break
    if learned == "n":
        print("This is how you play blackjack:")
        time.sleep(2)
        print("First, you gain 2 cards.")
        time.sleep(2)
        print("You got an", draw_card(cards)[0], "and a", draw_card(cards)[0] + ".")
        time.sleep(4)
        print("Now you have to hit (gain another card) or stand (stop gaining cards).")
        time.sleep(5)
        print("If you get a value of 21, you win!")
        time.sleep(2)
        print("Kings, Jacks, and Queens are worth 10.")
        time.sleep(2)
        print("Aces can be worth 1 or 11, depending on what benefits you most.")
        time.sleep(2)
        print("Alright! You're ready to play!")
        time.sleep(1)
    else:
        return "y"

def count_val(hand):
    total = 0
    ace_count = 0
    
    for card in hand:
        if card[1] == 1:
            ace_count += 1
        total += card[1]
    
    while total + 10 <= 21 and ace_count > 0:
        total += 10
        ace_count -= 1

    return total

def place_bet():
    global pot, chips
    while True:
        try:
            bet_amount = int(input(f"How much do you bet out of your {chips} chips? [int] "))
            if bet_amount <= 0:
                print("Bet must be a positive integer.")
                continue
            if bet_amount > chips:
                print(f"You cannot bet more than your total chips ({chips}).")
                continue
            
            affir = input(f"You bet {bet_amount} chips. Are you sure about this? [Y/N] ").strip().lower()
            if affir == "y":
                chips -= bet_amount
                pot += bet_amount * 2
                return chips, pot
            elif affir == "n":
                print("Choose a new bet.")
            else:
                print("Please enter 'Y' or 'N'.")
        
        except ValueError:
            print("Please enter a valid integer.")

def action(hand):
    global chips, pot
    action = False
    while True:
        hit_input = input("Hit, stand, fold, or raise. [H/S/F/R] ").strip().lower()
        if hit_input not in ["h", "s", "f", "r"]:
            print("Type hit, stand, fold, or raise.")
            continue
        
        if hit_input == "h": # Hit code
            new_card = draw_card(cards)
            hand.append(new_card)
            print("Your current cards are:")
            for card in hand:
                print(card[0])
            total = count_val(hand)
            print(f"Your total is: {total}")
            if total > 21:
                print("You busted!")
                return True  # Return bust status
            if total == 21:
                print("You got 21!")
                return False  # Not bust, but hit resulted in 21
        elif hit_input = "r": # Raise
            while True:
                try:
                    raise_amount = int(input(f"How much do you bet out of your {chips} chips? [int] "))
                    if raise_amount <= 0:
                        print("Raise amount must be a positive integer.")
                        continue
                    if raise_amount > chips:
                        print(f"You cannot raise more than your total chips ({chips}).")
                        continue
                    
                    affir = input(f"You raise by {raise_amount} chips. Are you sure about this? [Y/N] ").strip().lower()
                    if affir == "y":
                        chips -= raise_amount
                        pot += raise_amount * 2
                        action = True
                        return chips, pot
                    elif affir == "n":
                        print("Raise by a new number.")
                    else:
                        print("Please enter 'Y' or 'N'.")
                
                except ValueError:
                    print("Please enter a valid integer.")      
         elif == "s":
             return False  # Not hitting, return not bust
         else:
             return True

def check_win(pcarray, dcarray):
    global chips, pot
    player_totals = [count_val(hand) for hand in pcarray]  # Check totals for all hands
    dealer_total = count_val(dcarray)

    print("The dealer's first card is", dcarray[0][0], "and the second is", dcarray[1][0] + ".")
    
    while dealer_total < 17:
        print("The dealer drew a new card!")
        time.sleep(1)
        new_card = draw_card(cards)
        dcarray.append(new_card)
        print("The dealer's current cards are:")
        for card in dcarray:
            time.sleep(1)
            print(card[0])
        dealer_total = count_val(dcarray)
        time.sleep(1)
        print(f"His total is: {dealer_total}")

    for i, player_total in enumerate(player_totals):
        print(f"Your total for hand {i + 1} is: {player_total}")
        if player_total > 21:
            print(f"You busted in hand {i + 1}! Dealer wins this hand.")
        elif dealer_total > 21 or player_total > dealer_total:
            print(f"You won {pot} chips on hand {i + 1}!")
            chips += pot  # Player wins, add pot to chips
        elif player_total < dealer_total:
            print(f"Dealer wins against hand {i + 1}!")
        else:
            print(f"It's a push for hand {i + 1} (both same value)!")
            chips += round(pot / 2)

    print(f"You have {chips} remaining!")

def reset_game():
    global pot, pcarray, dcarray
    pot = 0
    pcarray.clear()
    dcarray.clear()

# Main game loop
has_learned = False  # Flag to track if the player has learned the rules
while chips > 0:  # Continue while the player has chips
    pot = 0
    pcarray = []  # Main array for player hands
    dcarray = []

    if not has_learned:
        if learn() == "y":
            has_learned = True  # Set the flag to true after learning

    place_bet()

    # Initial dealing of cards
    pcarray.append([draw_card(cards), draw_card(cards)])  # Create a new hand
    dcarray = [draw_card(cards), draw_card(cards)]

    print("Your cards are:")
    for card in pcarray[0]:  # Display the first hand's cards
        print(card[0])
    if count_val(pcarray[0]) == 21:
        print("It's a natural BLACKJACK!")
        check_win(pcarray, dcarray)
        continue
    
    print("The dealer's visible card is:", dcarray[0][0])

    # Player's turn for each hand
    for i in range(len(pcarray)):
        print(f"\nPlaying Hand {i + 1}:")
        bust = hit(pcarray[i])  # Pass each hand to the hit function
        if not bust:  # Only check win if the player has not busted
            check_win(pcarray, dcarray)

    play_again = input("Do you want to play again? [Y/N] ").strip().lower()
    if play_again != "n":
        continue
    else:
        print("Thanks for playing!")
        break
