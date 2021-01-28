print('BlackJack')

import random

# deck trumpを作成
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4

#  exit
def exit():
    print('お疲れ様でした')

# play_again
def play_again():
    again = input('続けますか？ (y/n):').lower()
    if again == 'y':
        game()
    else:
        print('終了')
        exit()

# deal
def deal():
    hand = []
    for index in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = 'J'
        if card == 12:
            card = 'Q'
        if card == 13:
            card = 'K'
        if card == 1:
            card = 'A'
        hand.append(card)
    return hand

# hit
def hit(hand):
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:
        card = 'J'
    if card == 12:
        card = 'Q'
    if card == 13:
        card = 'K'
    if card == 1:
        card = 'A'
    hand.append(card)
    return hand

# score
def total(hand):
    score = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            score += 10
        elif card == 'A':
            if score >= 11:
                score += 1
            else:
                score += 11
        else:
            score += card
    return score

# result
def result(player_hand, dealer_hand):
    print('\nResult')
    print(f'player-hand:{player_hand},total:{total(player_hand)}')
    print(f'dealer-hand:{dealer_hand},total:{total(dealer_hand)}')
    if total(player_hand) > total(dealer_hand):
        print('You Win!')
    elif total(player_hand) == total(dealer_hand):
        print('Draw!')
    else:
        print('You Lose!')
    play_again()

# game
def game():
    player_hand = deal()
    dealer_hand = deal()
    print(f'\ndealer-hand:[{dealer_hand[0]}]')
    print(f'player-hand:{player_hand},total:{total(player_hand)}')
    if total(player_hand) == 21:
        print('BlackJack!!')

    choice = 0

    while choice != quit:
        choice = input('stand/hit:').lower()
        if choice == 'hit':
            print('\nHit')
            hit(player_hand)
            print(f'player-hand-hit:{player_hand},total:{total(player_hand)}')
            if total(player_hand) >21:
                print('bust, You Lose...')
                choice = quit
                play_again()

        elif choice == 'stand':
            print('\nStand')
            print(f'dealer-hand:{dealer_hand},total:{total(dealer_hand)}')
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(f'dealer-hand-hit:{dealer_hand},total:{total(dealer_hand)}')
                if total(dealer_hand) > 21:
                    print('dealer bust, You Win')
                    choice = quit
                    play_again()

            choice = quit
            result(player_hand,dealer_hand)

game()

