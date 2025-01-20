import unittest
from BLACKJACK import Card, Deck, Hand, Chips, take_bet, hit, hit_or_stand, show_partially, show_all
class Test_cardclass(unittest.TestCase):
	def test_card(self):
		card_1 = Card('Clubs','King')
		self.assertEqual(card_1.suit,'Clubs')
		self.assertEqual(card_1.rank,'King')
		self.assertEqual(card_1.value, 10)
	def card_representation(self):
		card_2 = Card('Clubs','Queen')
		self.assertEqual(str(card), 'Queen of CLubs')
class Test_deckclass(unittest.TestCase):
	def deck_checker(self):
		deck = Deck()
		self.assertEqual(len(deck.deck), 52)
	def deck_print_checker(self):
		unique_cards = set(str(card) for card in deck.deck)
		self.assertEqual(len(unique_cards), 52)
	def shuffler_check(self):
		deck = Deck()
		original_deck = deck.deck[:]
		deck.shuffle()
		self.assertNotEqual(original_deck, deck.deck)
		self.assertEqual(len(deck.deck), len(original_deck))
	def deal_checker(self):
		deck = Deck()
		dealt_card = deck.deal()
		self.assertEqual(len(deck.deck), 51)
		self.assertNotIn(dealt_card, deck.deck)
class Test_handclass(unittest.TestCase):
	def add_card_checker(self):
		cards = []
		sample_card = ('Spades', 'Ace')
		cards.append(sample_card)
		self.assertIn(sample_card, cards)
	def adjustment_for_ace_case1(self):
		hand = Hand()
		hand.add_card('Spades', 'Six')
		hand.add_card('Clubs', 'Five')
		hand.add_card('Hearts', 'Three')
		self.assertEqual(hand.value, 14)
	def adjustment_for_ace_case2(self):
		hand = Hand()
		hand.add_card('Spades', 'Six')
		hand.add_card('Clubs', 'Five')
		hand.add_card('Hearts', 'Ace')
		self.assertEqual(hand.value, 12)
	def adjustment_for_ace_case3(self):
		hand = Hand()
		hand.add_card('Spades', 'Six')
		hand.add_card('Clubs', 'Ace')
		hand.add_card('Hearts', 'Ace')
		self.assertEqual(hand.value, 8)
	def adjustment_for_ace_case4(self):
		hand = Hand()
		hand.add_card('Spades', 'Six')
		hand.add_card('Clubs', 'Nine')
		hand.add_card('Hearts', 'Eight')
		self.assertEqual(hand.value, 23)
class Test_chipsclass(unittest.TestCase):
	def attribute_checker(self):
		chips = Chips()
		chips.total = 500
		chips.bet = 0
		self.assertEqual(chips.total, 500)
		self.assertEqual(chips.bet, 0)
	def win_bet_checker(self):
		chips = Chips()
		chips.total = 500
		chips.bet = 100
		chips.win_bet()
		self.assertEqual(chips.win_bet(), 600)
	def loss_bet_checker(self):
		chips = Chips()
		chips.total = 500
		chips.bet = 100
		chips.loss_bet()
		self.assertEqual(chips.loss_bet(), 400)