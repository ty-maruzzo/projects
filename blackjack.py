import random
from collections import defaultdict
suits = ['Clubs','Suits','Diamonds','Hearts']
ranks = ['2','3','4','5','6','7','8','9','10','J','K','Q','A']
deck = defaultdict(list)
for i in suits:
    deck[i].extend(ranks)
cards = [(suit, rank) for suit, rank in deck.items() for rank in ranks]
print(cards)
def fisher_yates_shuffle(deck):
   
    for i in range(len(deck)-1,0,-1):
        k = random.randint(0,i)
        deck[i],deck[k] = deck[k], deck[i]
        shuffled_dict = [k for k in deck]
    return shuffled_dict
print(fisher_yates_shuffle(cards))
ask_user = input('Do you want to play BlackJack?  Y/N ').lower()
while True:
    if ask_user == 'y':
        dealer_hand = deck
        player_hand_suit = random.choice(list((deck.keys())))
        player_hand_rank = random.choice(deck[player_hand_suit])
        dealer_hand[player_hand_suit].remove(player_hand_rank)
        print(player_hand_suit,player_hand_rank)
        print(dealer_hand)
        
    ask_user_card = input('Hit or Stand? ').lower()
    if ask_user_card == 'hit':
        player_hand_suit = random.choice(list((deck.keys())))
        player_hand_rank = random.choice(deck[player_hand_suit])
        dealer_hand[player_hand_suit].remove(player_hand_rank)
        print(player_hand_suit,player_hand_rank)
        print(dealer_hand)
    if ask_user == 'n':
        break
