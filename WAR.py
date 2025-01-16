suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
import random
class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffler(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
    
class Player():

    def __init__(self,name):
        self.name = name
        self.all_cards = []
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def remove_one(self):
        return self.all_cards.pop(0)
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards"

#CREATING PLAYERS
Player_one = Player("One")
Player_two = Player("Two")
#CREATING THE GAME DECK
Game_deck = Deck()
Game_deck.shuffler()
#GIVING THE PLAYER THEIR CARDS
for x in range(26):
    Player_one.add_cards(Game_deck.deal_one())
    Player_two.add_cards(Game_deck.deal_one())
#CREATING THE OUTTER WHILE LOOP
game_on = True
round_number = 0
while game_on == True:
    #THE BELOW CODE IS TO CHECK THE NUMBER OF CARDS
    round_number = round_number + 1
    print(f"Round {round_number}")
    if len(Player_one.all_cards) == 0:
        print("Player one is out of cards\n Player two has won the game!!!!")
        game_on = False
        break
    if len(Player_two.all_cards) == 0:
        print("Player two is out of cards\n Player one has won the game!!!!")
        game_on = False
        break
    #STARTING A NEW ROUND AND RESETTING THE CARDS ON THE TABLE
    Player_one_cards = []
    Player_one_cards.append(Player_one.remove_one())
    Player_two_cards = []
    Player_two_cards.append(Player_two.remove_one())

    #STARTING THE WAR LOGIC
    at_war = True
    while at_war == True:
        if Player_one_cards[-1].value > Player_two_cards[-1].value:
            Player_one.add_cards(Player_one_cards)
            Player_one.add_cards(Player_two_cards)
            at_war = False
        elif Player_one_cards[-1].value < Player_two_cards[-1].value:
            Player_two.add_cards(Player_one_cards)
            Player_two.add_cards(Player_two_cards)
            at_war = False
        elif Player_one_cards[-1].value == Player_two_cards[-1].value:
            print("It is time for WAR")
            if len(Player_one.all_cards) < 5:
                print("Player One has insufficient number of cards hence cannot continue the game.")
                print("Player Two wins!!!!")
                at_war = False
                game_on = False
            elif len(Player_two.all_cards) < 5:
                print("Player Two has insufficient number of cards hence cannot continue the game.")
                print("Player One wins!!!!")
                at_war = False
                game_on = False
            else:
                for num in range(5):
                    Player_one_cards.append(Player_one.remove_one())
                    Player_two_cards.append(Player_two.remove_one())







