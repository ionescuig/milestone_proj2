"""
Blackjack Game
"""

import os
from random import choice

class Deck(object):
    '''
    Defines the deck (1 deck of 52 cards)
    '''

    def __init__(self,
                 c_rank=['2','3','4','5','6','7','8','9','10','J','Q','K','A']*4,
                 c_suit=['Spade','Heart','Diamond','Club']):
        self.c_rank = c_rank
        self.c_suit = c_suit

    def deck_start(self):
        self.c_rank = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']*4
        self.c_suit = ['Spade','Heart','Diamond','Club']

    def deck_play(self, rank):
        self.c_rank -= rank

    def deck_shuffle(self):
        rank = choice(self.c_rank)
        suit = choice(self.c_suit)
        return (rank, suit)

class Player(object):
    '''
    Defines the player's name and his bankroll
    '''
    
    def __init__(self, name='Player', bankroll=100):
        self.name = name
        self.bankroll = bankroll

    def win(self,bet):
        self.bankroll += bet

    def lose(self,bet):
        self.bankroll -= bet
        

class PlayerHand(object):
    '''
    Defines player's hand
    which will be a list of touplles
    '''
    def __init__(self,hand=[],total=0):
        self.hand = hand
        self.total = total

    def add_card(self):
        self.hand.append(deck.deck_shuffle())

def start_amount():
    '''
    Asks for starting amount
    '''

    os.system('cls')
    while True:
        try:
            print 'Players will start with the same amount of money'
            amount = int(raw_input('Please enter the amount (100 or more): '))
        except:
            print 'This is not a number'
        else:
            if amount >= 100:
                return amount
                break
            else:
                continue

            
def bet():
    while True:
        try:
            b = int(raw_input('Please enter your bet: '))
            if b > player.bankroll:
                print 'The amount you enter is too high. Please try again.'
            else:
                break
        except:
            print 'This is not a real bet. Please try again.'
    return b


def hit():
    while True:
        p_hand.add_card()
        total = 0
        list_a = []
        for i in p_hand.hand:
            if i[0] == int(i[0]):
                total += int(i[0])
            elif i[0] in ['J','Q','K']:
                total += 10
            elif i[0] == 'A':
                if (total + 11) <= 21:
                    total += 11
                    list_a.append('A')
                else:
                    total += 1
        if total > 21:
            for j in list_a:
                if j == 'A':
                    total -= 10
                    list_a.remove('A')
                    break
        if total > 21:                    
            break
        return total


def table():
    '''
    Display
    '''
    
    os.system('cls')
    print ''
    print '     Bet:', repr(bet).rjust(10)
    print '\n'
    
    print '  Player', repr(player.bankroll).rjust(10)
    for i in p_hand.hand:
        print i[0].rjust(8), i[1]
    print '\n'
    
    print '  Dealer'
    for i in d_hand.hand:
        print i[0].rjust(8), i[1]
    
    

s_amount = start_amount()                   # asks for starting amount
player = Player('Player', s_amount)         # initialize Player
dealer = Player('Dealer')                   # initialize Dealer
deck = Deck()                               # initialize Deck

os.system('cls')
bet=bet()                                   # asks for bet

p_hand = PlayerHand([],0)
p_hand.add_card()
p_hand.add_card()


d_hand = PlayerHand([],0)
d_hand.add_card()

table()                                     # displays the table

raw_input()
