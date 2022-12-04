import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
wager = [10, 20, 50, 100, 200]


counter_cards = 104

cards_player1 = []
cards_dealer = []

wager_player = 0
wager_dealer = 0


score_p1 = sum(cards_player1)
score_d = sum(cards_dealer)

account_player1 = 1000
account_dealer = 1000
curr_wager_player = 0
curr_wager_dealer = 0
wager_on_table = curr_wager_dealer + curr_wager_player
def initial_dealing_player():
    for i in range(0,2):
        i = random.choice(cards)
        cards_player1.append(i)

def serve_hit_dealer():
    for i in range(0,1):
        i = random.choice(cards)
        cards_dealer.append(i)

def hit_player1():
    for hit_card in range(0, 1):
        hit_card = random.choice(cards)
        cards_player1.append(hit_card)

def double_down():
    for hit_card in range(0, 1):
        hit_card = random.choice(cards)
        cards_player1.append(hit_card)

def split_cards():
    cards_player1.pop(-1)
    score_d = 0


def surrender():
    score_p1 = cards_player1.clear()

# def doublwager():
def random_wager():
    x = random.choice(wager)



actions ={
    "hit": hit_player1,
    "stand": serve_hit_dealer,
    "double down": double_down,
    "split": split_cards,
    "surrender": surrender
    }

# initial deal
while counter_cards > 0:
    initial_dealing_player()
    print(f"Your cards are {cards_player1}")
    score_p1 = sum(cards_player1)
    print(f"Your score is {score_p1}")
    print("Your wager  is 100$")
    print()
    account_player1 -= 100
    curr_wager_player +=100
    counter_cards -= 1
    counter_cards -= 1


    serve_hit_dealer()
    print(f"Dealer's cards are {cards_dealer} |🃏| ")
    score_d = sum(cards_dealer)
    print(f"Dealer's score is {score_d}")
    print("Dealer's wager is 100$")
    print()
    account_dealer -= 100
    curr_wager_dealer += 100
    counter_cards -= 1

    print(f"Total wager ${curr_wager_dealer + curr_wager_dealer}")
    print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
    print()



    #  update wager

    more_wage_dbl = input("Double the wager $? y/n ->")
    if more_wage_dbl =='y':
        account_player1 -= 100
        curr_wager_player += 100
        print(f"Your wager is ${curr_wager_player}")

        account_dealer -= 100
        curr_wager_dealer += 100
        print(f"Dealer's wager is ${curr_wager_dealer}")
        print()
        print(f"Total wager ${curr_wager_dealer + curr_wager_player}")
        print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
        print()
    more_wage = input("Increase the wager? y/n ->")
    if more_wage == 'y':

        for wage in wager:
            print(wage)
        choice_wage = int(input("$ "))
        account_player1 -= choice_wage
        curr_wager_player += choice_wage

        account_dealer -= choice_wage
        curr_wager_dealer += choice_wage
        print(f"Your wager is ${curr_wager_player}")
        print(f"Dealer's wager is ${curr_wager_dealer}")
        print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
        print()


    for key in actions:
        print(f"$$$-{key}-$$$")


    score_is_under21 = True
    while score_is_under21:

        if score_p1 == 21:
            print("BlackJack! You win!")
            print(f"Your cards are {cards_player1}")
            print()
            score_p1 = sum(cards_player1)
            account_player1 += curr_wager_player + curr_wager_dealer
            print(score_p1)

            print(f"Dealer's cards are {cards_dealer}")
            score_d = sum(cards_dealer)
            print(score_d)
            print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
            break


        elif score_d == 21:
            print("BlackJack! You lose!")
            print(f"Your cards are {cards_player1}")
            print()
            score_p1 = sum(cards_player1)
            print(score_p1)
            print()
            print(f"Dealer's cards are {cards_dealer}")
            score_d = sum(cards_dealer)
            print(score_d, end="")
            print(f" ${account_dealer + curr_wager_player + curr_wager_dealer}")
            print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
            break
        elif score_p1 > 21 and score_d <21:
            print("You lose!")
            print(f"Your cards are {cards_player1}")
            print(f"Your score is {score_p1}")
            print()
            score_p1 = sum(cards_player1)

            print(f"Dealer's cards are {cards_dealer} ")
            score_d = sum(cards_dealer)
            print(score_d)
            print(f" ${account_dealer + curr_wager_player + curr_wager_dealer }")
            print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
            break

        elif score_d > 21 and score_p1 <21:
            print("You win!")
            print(f"Your cards are {cards_player1}")
            score_p1 = sum(cards_player1)
            account_player1 += curr_wager_player + curr_wager_dealer
            print(f"Your score is {score_p1}")
            print()

            print(f"Dealer's cards are {cards_dealer} # ")
            score_d = sum(cards_dealer)
            print(score_d)
            print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
            break

        elif score_p1 == 21 and score_d == 21:
            print("Push!")
            print(f"Your cards are {cards_player1}")
            score_p1 = sum(cards_player1)
            print(score_p1)
            print(f" ${account_player1}")
            print()
            print(f"Dealer's cards are {cards_dealer} # ")
            score_d = sum(cards_dealer)
            print(score_d)
            print(f" ${account_dealer}")
            print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
            break

        elif score_p1 == score_d:
            print("Play Again!")
            print(f"Your cards are {cards_player1}")
            score_p1 = sum(cards_player1)
            account_player1 += curr_wager_player
            print(score_p1)

            print()
            print(f"Dealer's cards are {cards_dealer} ")
            score_d = sum(cards_dealer)
            print(score_d)

            print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
            break

        else:
            print()
            q1 = input("hit(h), stand(s), double_down(dd), split(p), surrender(u)?")
            print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
            if q1 == "h":
                hit_player1()
                score_p1 = sum(cards_player1)
                if cards_player1[-1] == 11 and score_p1 >= 21:
                    cards_player1[-1] = 1
                    score_p1 = sum(cards_player1)
                serve_hit_dealer()
                score_d = sum(cards_dealer)
                counter_cards -= 1
                if score_p1 < 21 and score_p1 > score_d:
                    print("You win!")
                    print(f"You hit {cards_player1[-1]}")
                    print(f"Your score is now {sum(cards_player1)}")
                    account_player1 += curr_wager_player + curr_wager_dealer
                    print()
                    print(f"Dealer pulls {cards_dealer[-1]}")
                    print(f"Dealer's score is now {sum(cards_dealer)}")
                    print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
                    break
                elif score_d < 21 and score_d > score_p1:
                    print("You lose!")
                    print(f"You hit {cards_player1[-1]}")
                    print(f"Your score is now {sum(cards_player1)}")
                    print()
                    print(f"Dealer pulls {cards_dealer[-1]}")
                    print(f"Dealer's score is now {sum(cards_dealer)}")
                    print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
                    break



            elif q1 == "s":
                serve_hit_dealer()
                counter_cards -= 1
                score_d = sum(cards_dealer)
                if score_d > score_p1 and score_d < 21:
                    print("You lose!")
                    print(f"Your score is {score_p1}")
                    print(f"Dealer's score is {score_d}")
                    print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
                    break

                elif score_p1 > 21 or score_d > 21:
                    score_is_under = False
                else:
                    print(f"Dealer pulled {cards_dealer[-1]}")
                    print(f"Dealer's score is now {score_d}")


            elif q1 == "dd":
                hit_player1()
                counter_cards -= 1
                curr_wager_player *= 2

            elif q1 =="p":
                print(f"You have doubled your wager ${curr_wager_player * 2}")
                account_player1 -=curr_wager_player
                split_cards()
                hit_player1()
                print(f"Your score is {score_p1}")
                serve_hit_dealer()
                print(f"Dealer's score is {score_d}")
                print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")


            elif q1 == "u":
                surrender()
                account_player1 += curr_wager_player / 2
                print("You drop the game")
                print(f"Your balance is  $ {account_player1}")
                print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")

    cards_player1.clear()
    cards_dealer.clear()
    curr_wager_player = 0
    curr_wager_dealer = 0
    print(f"Your balance is ${account_player1}")
    print(f"🃏♣🃏♡🃏♢🃏♣🃏♡🃏♤🃏♢🃏♣🃏♡🃏♤🃏♢🃏")
    print()
    print("$-$-$-NEW ROUND-$-$-$")
    print()



