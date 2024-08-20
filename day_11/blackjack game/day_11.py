
import random
from art_week2 import blackjack_logo
print(blackjack_logo)
card_deck=[11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer_hand=[]
player_hand=[]
##########################################################################################
def user_over_21_and_ace(player_hand):
    if sum(player_hand)>21 :                                                     # player toke to much and we need to check if he got an ace
        if 11 in player_hand:
            index_player=player_hand.index(11)
            player_hand[index_player]=1
            hit_or_miss(player_hand)
        else:                                                                   # no ace and hand sum is above 21
            return player_hand
    else:
        return  player_hand








########################################################################################
def dealer_turn(dealer_hand):
    print("its dealer turn")
    print(dealer_hand)
    while sum(dealer_hand)<=16:
        print("dealer toke a card")
        dealer_hand.append(random.choice(card_deck))
        print(dealer_hand)
    if sum(dealer_hand)>21:
        if 11 in dealer_hand:
            index=dealer_hand.index(11)
            dealer_hand[index]=1
            print("dealer transmit ace to 1")
            dealer_turn(dealer_hand)
        else:
            return dealer_hand
    else:
        return dealer_hand

########################################################################################
#                                hit or miss function                                  #
########################################################################################
def hit_or_miss(player_hand):
    while sum(player_hand)<21: # the loop for hit and pass of the player

        print(player_hand)
        print(sum(player_hand))
        hit_or_pass=input("do you want to hit or do you want to pass :\n\n").lower()
        if hit_or_pass=="hit":
            player_hand.append(random.choice(card_deck))
            print("you drew a card your hand is :")
            print(player_hand)
            if sum(player_hand)>21:
                user_over_21_and_ace(player_hand)
        elif hit_or_pass=="pass":
            return player_hand



#########################################################################################################################################
###############################################################
#                     blackjec function                       #
###############################################################
def bleckjeck():
    print("you delt a hand:")
    player_hand=random.sample(card_deck,2)                     # create a list for the user
    dealer_hand=random.sample(card_deck,2)                      # create a list for the dealer
    print(player_hand)                                         # shoe your hand
    print("dealer got cards and the card shown is :")
    print(dealer_hand[0])                                            #show dealer 1 card
    player_hand_sum=sum(player_hand)                           #aquire the sum of the hands
    dealer_hand_sum=sum(dealer_hand)                          # same
    if player_hand_sum==21:                                   # check if the game ends at the start
        print("you win")                                                     # user hand is not 21
        return
    elif player_hand_sum<21:
        player_hand=hit_or_miss(player_hand)


    if  dealer_hand_sum<16 :                              # the player didnt lose and now its the turn of the dealer
        print("dealer decided to take a card")
        dealer_hand=dealer_turn(dealer_hand)
        print("dealer finish cards")




#####################################################################################################################
#                                                      compare                                                      #
######################################################################################################################
    print(f"the dealer hand is : {dealer_hand} and ths sum is : {sum(dealer_hand)}")
    print(f"the player hand is {player_hand} and the sum is : {sum(player_hand)} ")

    if sum(player_hand)>21:
        print("you lose")
    elif sum(dealer_hand)>21:
        print("you win")
    else:
        if sum(player_hand)>sum(dealer_hand):
            print("you win")
        elif sum(player_hand)==sum(dealer_hand):
            print("drew")
        else:
            print("you lose")

#########################################################################################################################


player_input=input("do you want to play blackjeck\n\n:").lower()    # ask if the user want to play
if player_input=="yes":                                             # enter the if statment to run the game
    bleckjeck()
else:
    print("ok thanks and good bye")
