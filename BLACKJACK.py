suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
import random

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp = deck_comp + '\n ' + card.__str__
        return "The deck is " + deck_comp

    def shuffler(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand():
    def __init__(self):
        # SELF.CARDS REPRESENTS THE CARDS GIVEN TO THE PERSON
        self.cards = []
        # SELF.VALUE REPRESENTS THE VALUE OF EACH CARD AND ADD IT REFERING FROM THE VALUES DICTIONARY
        self.value = 0
        # SELF.ACES
        self.aces = 0

    def add_card(self, card):
        # CARD OBJECT IS TAKEN FROM DECK.DEAL() AND IT IS APPENDED INTO THE SELF.VALUE
        self.cards.append(card)
        self.value = self.value + values[card.rank]
        # CHECK IF THE CARD IS AN ACE AND ADD IT TO THE SELF.ACES
        if card == "Ace":
            self.aces = self.aces + 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces != 0:
            self.value = self.value - 10
            self.aces = self.aces - 1
        # HERE WE ARE CHECKING FOR TWO CONDITIONS ONE WHICH IS WHETER THE SUM IS GREATER THAN 21 OR NOT AND SECOND IS THE NUMBER OF ACES IS NOT ZERO.

class Chips():
    def __init__(self, total=500):
        # HERE BY GIVING A MINIMUM VALUE OF 500 IN THE BRACKET PLAYER START WITH 500 CHIPS BUT IF HTEY WANT MORE CHIPS THEY CAN ENTER THE VALUE TO THEIR LIKING.
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total = self.total + self.bet

    def loss_bet(self):
        self.total = self.total - self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Please enter the number of chips you want to bet? '))
        except:
            print('Sorry that is not an integer, Please enter an number that is an integer!')
        else:
            if chips.bet > chips.total:
                print(f'The amount of you have entered exceeds your available amount of chips, You have {chips.total}')
            else:
                break
# IN THE ABOVE FUNC WE ARE USING AN TRY, EXCEPT AND ELSE EXCEPTION HANDLING METHOD TO TAKE IN PLAYER BET.

def hit(deck, hand):
    hit_card = deck.deal()
    hand.add_card(hit_card)
    hand.adjust_for_ace()
# IN THE ABOVE FUNC WE ARE WRITING IF THE PLAYER WANTS TO HIT

def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input('Do you want to hit or stand, Enter h for hit and s for stand: ')
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands, it is Dealer's turn")
            playing = False
        else:
            print('Try again')
            continue
        break

def show_partially(player, dealer):
    print('\nDealers hand: ')
    print('\nFirst card hidden')
    print(dealer.cards[1])
    print('Players hand: ')
    for x in player.cards:
        print(x)
# THE ABOVE FUNC ONLY SHOWS PARTIALL CARDS INITIALLY

def show_all(player, dealer):
    print("\nDealers hand: ")
    for x in dealer.cards:
        print(x)
    print(f"The value of Dealers cards is {dealer.value}")
    print("\nPlayers cards: ")
    for x in player.cards:
        print(x)
    print(f"The value of Players cards is {player.value}")
# THE ABOVE FUNC IS FOR SHOWING AND CALCULATING THE VALUE

def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.loss_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.loss_bet()

def push(player, dealer):
    print("Dealer and Player tie! It's a push.")

playing = True

def main():
    # GAME CODE
    global playing
    while True:
        print("Welcome to Blackjack! Get as close to 21 as you can without going over it, Dealer hits until they reach 17. Aces count as 1 or 11")

        deck = Deck()
        deck.shuffler()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_chips = Chips()

        take_bet(player_chips)

        show_partially(player_hand, dealer_hand)

        while playing:
            hit_or_stand(deck, player_hand)

            show_partially(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            show_all(player_hand, dealer_hand)
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        print(f"\nThe Player has {player_chips.total}")

        new_game = input("Do you want to play a new game? Enter 'y' for Yes or 'n' for No: ")
        if new_game[0].lower() == 'y':
            continue
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
