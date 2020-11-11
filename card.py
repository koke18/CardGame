from random import shuffle
import math


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
        self.value = values[rank] 

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck():

    def __init__(self):
        self.card_deck = [] 
        for i in ranks:
            for j in suits: 

                new_card = Card(i, j)
                self.card_deck.append(new_card)
    
    def shuffle_cards(self):
        shuffle(self.card_deck)
    
    def deal(self):
        return self.card_deck.pop() 


class Player():

    def __init__(self, name):

        self.user_cards = [] 
        self.name = name
    
    def play_card(self):
        return self.user_cards.pop(0) 

    def add_card(self, new_cards):
        if type(new_cards) == type(self.user_cards):
            self.user_cards.extend(new_cards)
        
        else:
            self.user_cards.append(new_cards)

    def __str__(self):
        return f'{self.name} has {len(self.user_cards)} card(s).'


def game():
    
    curr_deck = Deck()
    curr_deck.shuffle_cards()

    player_1 = Player("Jond")
    player_2 = Player("Felix") 


    for i in range(0, 52):
        if i%2 == 0:
            player_1.user_cards.append(curr_deck.deal())
        
        if i%2 != 0:
            player_2.user_cards.append(curr_deck.deal())


    len_player_1 = len(player_1.user_cards)
    len_player_2 = len(player_2.user_cards)

    while len_player_1 > 0 and len_player_2 > 0: 
        if (len(player_1.user_cards) == 0) or (len(player_2.user_cards) == 0):
            break

        one_value = player_1.play_card()
        two_value = player_2.play_card() 

        if (values[one_value.rank] > values[two_value.rank]):
            win_hand_1 = [one_value, two_value]
            player_1.add_card(win_hand_1)
            print(one_value, two_value)
            print("\none")
        
        elif (values[one_value.rank] < values[two_value.rank]):
            win_hand_2 = [two_value, one_value]
            player_2.add_card(win_hand_2)
            print(two_value, one_value)
            print("\ntwo")
        
        else:
            total_win = [one_value, two_value] 
            
            for i in range(3): 
                total_win.append(player_1.play_card())
                total_win.append(player_2.play_card())

            kept = True
            while kept: 
                compare_1 = player_1.play_card()
                compare_2 = player_2.play_card() 
                total_win.extend([compare_1, compare_2])
                
                if (values[compare_1.rank] > values[compare_2.rank]):
                    player_1.add_card(total_win)
                    print("\none")
                    kept = False
                

                elif (values[compare_1.rank] < values[compare_2.rank]):
                    player_2.add_card(total_win)
                    print("\ntwo")
                    kept = False


            print(f'{two_value} = {one_value}')

            for i in total_win:
                print(i) 
  
    
    print(len(player_1.user_cards))
    print(len(player_2.user_cards))

game() 

