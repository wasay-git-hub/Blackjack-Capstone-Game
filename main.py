import art
import random
print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def initialization():
    player_cards = []
    comp_cards = []
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    player_cards.append(card1)
    player_cards.append(card2)

    comp1 = random.choice(cards)
    comp_cards.append(comp1)
    initial_sum = card1 + card2
    comp_sum = comp1
    
    print(f"Your cards: [{card1},{card2}]\nCurrent Score: {initial_sum}")
    print(f"Computer's first card: {comp1}. 2nd is unturned.\n")
    return player_cards, comp_cards, initial_sum, comp_sum

player_cards, comp_cards, initial_sum, comp_sum = initialization()

def ask(initial_score, comp_score, player_cards, comp_cards):
    resume = True
    while resume:
        choice1 = input("Type 'y' to hit (get another card), type 'n' to pass.\n")

        if choice1 == 'y':
            card = random.choice(cards)
            player_cards.append(card)
            initial_score += card

            all_cards = ",".join(str(card) for card in player_cards)
            print(f"\nYour cards: [{all_cards}]\nCurrent Score: {initial_score}")

            allComp_cards = ",".join(str(card) for card in comp_cards)
            print(f"Computer's card(s): {allComp_cards}\n")

            if initial_score > 21 and 11 in player_cards:
                player_cards[player_cards.index(11)] = 1
                initial_score -= 10
            elif initial_score > 21:
                print("BUST!! You Lost. Your score exceeded 21.")
                return


        elif choice1 == 'n':
            resume = False

            all_cards = ",".join(str(card) for card in player_cards)
            print(f"\nYour cards: [{all_cards}]\nCurrent Score: {initial_score}")

            while comp_score < 17:

                if comp_score < 17:
                    print("\nComputer will have to draw another card as its score is less than 17.\n")

                comp_card = random.choice(cards)
                comp_cards.append(comp_card)
                comp_score += comp_card

                allComp_cards = ",".join(str(card) for card in comp_cards)
                print(f"Computer's card(s): {allComp_cards}\nComputer's Score: {comp_score}\n")

                if comp_score > 21 and 11 in comp_cards:
                    comp_cards[comp_cards.index(11)] = 1
                    comp_score -= 10
                elif comp_score > 21:
                    print("BUST!! You Won. Your score exceeded 21.")
                    return


            print("-" * 50)  # formatting
            if comp_score > initial_score:
                ",".join(str(card) for card in player_cards)
                print(f"Your final hand: [{player_cards}]")
                print(f"Your Score: {initial_score}")
                allComp_cards = ",".join(str(card) for card in comp_cards)
                print(f"Computer's final hand: [{allComp_cards}]")
                print(f"Computer's Score: {comp_score}")
                print("You Lost!")

            elif initial_score > comp_score:
                ",".join(str(card) for card in player_cards)
                print(f"Your final hand: [{player_cards}]")
                print(f"Your Score: {initial_score}")
                allComp_cards = ",".join(str(card) for card in comp_cards)
                print(f"Computer's final hand: [{allComp_cards}]")
                print(f"Computer's Score: {comp_score}")
                print("You Won!")

            elif initial_score == comp_score:
                ",".join(str(card) for card in player_cards)
                print(f"Your final hand: [{player_cards}]")
                print(f"Your Score: {initial_score}")
                allComp_cards = ",".join(str(card) for card in comp_cards)
                print(f"Computer's final hand: [{allComp_cards}]")
                print(f"Computer's Score: {comp_score}")
                print("A Draw.")

            print("-" * 50)  # formatting

        else:
            print("Invalid Choice.")

ask(initial_sum,comp_sum, player_cards, comp_cards)

another_match = input("Do you want another match? Type 'y' for yes and 'n' for no.\n")
cont = True

if another_match == 'n':
    cont = False
    print("\nThanks for playing!\n")

while cont:
    print("\n" + "-" * 50)  # formatting
    print("Starting a new round of Blackjack")  # formatting
    print("-" * 50 + "\n")  # formatting

    player_cards, comp_cards, initial_sum, comp_sum = initialization()
    ask(initial_sum, comp_sum, player_cards, comp_cards)

    another_match = input("Do you want another match? Type 'y' for yes and 'n' for no.\n")

    if another_match == 'n':
        print("\nThanks for playing!\n")
        cont = False
    elif another_match == 'y':
        cont = True
    else:
        print("Invalid Choice. A 'no' is assumed.")
        print("Thanks for playing!\n")
