import random
from collections import defaultdict
suits = ['Clubs','Suits','Diamonds','Hearts']
ranks = ['2','3','4','5','6','7','8','9','10','J','K','Q','A']
deck = defaultdict(list)
for i in suits:
    deck[i].extend(ranks)
cards = [[suit, rank] for suit, rank in deck.items() for rank in ranks]

rank_scores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def calculate_hand_score(hand):
    score = 0
    aces = 0
    for card in hand:
        rank = card[1]
        score += rank_scores[rank]
        if rank == 'A':
            aces += 1
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def fisher_yates_shuffle(deck):
   
    for i in range(len(deck)-1,0,-1):
        k = random.randint(0,i)
        deck[i],deck[k] = deck[k], deck[i]
        shuffled_dict = [k for k in deck]
    return shuffled_dict
deck = (fisher_yates_shuffle(cards))
ask_user = input('Do you want to play BlackJack?  Y/N ').lower()
if ask_user == 'y':
        #Start of Game

        dealer_hand_shown = random.choice(deck)
        deck.remove(dealer_hand_shown)
        dealer_hand_hidden = random.choice(deck)
        deck.remove(dealer_hand_hidden)
        dealer_hand = list()
        dealer_hand.append(dealer_hand_hidden)
        dealer_hand.append(dealer_hand_shown)
        player_hand = random.choice(deck)
        hand = list()
        hand.append(player_hand)
        print(f'Player has a  {player_hand[1]} of {player_hand[0]}\n')
        deck.remove(player_hand)
        print(f'Dealer has {dealer_hand_shown[1]} of {dealer_hand_shown[0]}')
        print('Dealer has a hidden card\n')
        dealer_hand_score = calculate_hand_score(dealer_hand)
if ask_user == 'n':
    exit()
while True:#this runs always
    ask_user_card = input('Hit or Stand? ').lower()
    if ask_user_card =='hit':
        player_hit = random.choice(deck)
        print(f'player has a {player_hit[1]} of {player_hit[0]}')
        hand.append(player_hit)
        deck.remove(player_hit)
        player_hand_score = calculate_hand_score(hand)
        print(f'Total Score: {player_hand_score}')
        if player_hand_score > 21:
            print("Game Over")
            print("Dealer Wins!")
            break
        if player_hand_score == 21:
            print("Game Over")
            print("Player Wins!")
    if ask_user_card == 'stand': #game ends no exceptions
        print("Game End \n")
        print("Player Score \n")
        for suit,rank in hand:
            print(f'Player has {rank} of {suit}')
        print(f'Player has a total score of:  {player_hand_score}')
        
        print('\n\n\n')
        while dealer_hand_score <= 16:#drawing dealer
            print("Dealer is now drawing")
            dealer_hit = random.choice(deck)
            dealer_hand.append(dealer_hit)
            dealer_hand_score = calculate_hand_score(dealer_hand)
            deck.remove(dealer_hit)
        print('\n')
        for suit,rank in dealer_hand:#print dealer score hand his hand
            print(f'Dealer has {rank} of {suit}')
        print(f'Dealer has a total score of: {dealer_hand_score}')
        if dealer_hand_score > 21:
            print(f'Player Wins with total score of {player_hand_score} and  dealer\'s score {dealer_hand_score} is over 21')
        elif dealer_hand_score == player_hand_score:
            print("Player and Dealer has same score, its a Tie! ")
        elif player_hand_score > dealer_hand_score and player_hand_score <=21:
            print('Player Wins! ')
        elif dealer_hand_score > player_hand_score and dealer_hand_score<= 21:
            print('Dealer Wins!')
        break
        