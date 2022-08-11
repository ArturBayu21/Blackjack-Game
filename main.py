import os
import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# ================= FUNCTION NEEDED ===================


def get_starting_card():
    '''return 2 random cards on list type'''
    random_cards = []
    for i in range(0, 2):
        random_num = random.randint(0, len(cards)-1)
        random_cards.append(cards[random_num])
    return random_cards


def get_another_card():
    '''return 1 random card (int type)'''
    random_num = random.randint(0, len(cards)-1)
    random_card = cards[random_num]
    return random_card


def get_computer_cards():
    '''return computer's card'''
    computer_cards = get_starting_card()
    cards_value = 0
    for each_card in computer_cards:
        cards_value += each_card
    while cards_value < 17:
        new_card = get_another_card()
        computer_cards.append(new_card)
        cards_value += new_card
    return computer_cards


def calculate_value(deck):
    '''return a value of the deck of card'''
    value = 0
    for each_card in deck:
        value += each_card
    return value


# =====================================================


start_game = True
user_deck = {}
computer_deck = {}

while start_game == True:
    wants_card = True
    user_controll = input(
        "Do you want to play the Blackjack game? type 'yes' or 'no' : ").lower()
    if user_controll == 'yes':
        os.system('cls')
        print(art.logo)
        # getting card for user
        user_deck["Cards"] = get_starting_card()
        user_deck["Value"] = calculate_value(user_deck["Cards"])
        # getting card for computer
        computer_deck["Cards"] = get_computer_cards()
        computer_deck["Value"] = calculate_value(computer_deck["Cards"])
        print(
            f"    Your cards: {user_deck['Cards']}, current_score: {user_deck['Value']}")
        print(f"    Computer's first card: {computer_deck['Cards'][0]}")
        # User want another card
        while wants_card == True:
            user_decision = input(
                "Type 'yes' if you want another card, type 'no' to pass : ").lower()
            if user_decision == 'yes':
                user_deck["Cards"].append(get_another_card())
                user_deck["Value"] = calculate_value(user_deck["Cards"])
                print(
                    f"    Your cards: {user_deck['Cards']}, current_score: {user_deck['Value']}")
                print(
                    f"    Computer's first card: {computer_deck['Cards'][0]}")
                # check wheater user get buzz
                if user_deck["Value"] > 21:
                    print(
                        f"    Your final hand : {user_deck['Cards']}, final score: {user_deck['Value']}")
                    print(
                        f"    Computer's final hand : {computer_deck['Cards']}, final score: {computer_deck['Value']}")
                    print("You went over, you lose 😭")
                    wants_card = False
            else:
                print(
                    f"    Your final hand : {user_deck['Cards']}, final score: {user_deck['Value']}")
                print(
                    f"    Computer's final hand : {computer_deck['Cards']}, final score: {computer_deck['Value']}")
                if computer_deck["Value"] > 21:
                    print("Opponent went over, You win 😍 ")
                elif user_deck["Value"] > computer_deck["Value"]:
                    print("You Win 😍 ")
                elif user_deck["Value"] < computer_deck["Value"]:
                    print("You Lose 😭 ")
                else:
                    print("It's a Draw! 😁")
                wants_card = False
    else:
        start_game = False
