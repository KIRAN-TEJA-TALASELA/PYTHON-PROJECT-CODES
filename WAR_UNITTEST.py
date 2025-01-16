import unittest
from WAR import Card, Deck, Player
class Test_card(unittest.TestCase):
	def test_card_attributes(self):
		card = Card('Spades', 'Jack')
		self.assertEqual(card.suit, 'Spades')
		self.assertEqual(card.rank, 'Jack')
		self.assertEqual(card.value, 11)

	def test_card_string_representation(self):
		card = Card('Spades', 'Jack')
		self.assertEqual(str(card), 'Jack of Spades')

class Test_deck(unittest.TestCase):
	def deck_class_attributes(self):
		deck = Deck()
		self.assertEqual(len(deck.all_cards), 52)
	def Test_deck_shuffler(self):
		deck = Deck()
		original_order = deck.copy()
		self.assertNotEqual(deck.all_cards, deck.copy())

class Test_player(unittest.TestCase):	
	def Test_player_attributes(self):
		player = Player("Player one")
		self.assertEqual(player.name, "Player one")
		self.assertEqual(len(player.all_cards), 0)
	def Test_add_cards(self):
		player = Player("Player one")
		sample_card_1 = ('Hearts', 'Five')
		sample_card_2 = ('Spades', 'Eight')

		player.add_cards(sample_card_1)
		self.assertEqual(len(player.all_cards), 1)

		player.add_cards(sample_card_2)
		self.assertEqual(len(player.add_cards), 2)

	def Test_player_str_case(self):
		player = Player("Player one")
		self.assertEqual(str(Player), "Player one has 0 cards")
class Test_game_logic(unittest.TestCase):
	def test_game_1(self):
		player_one = Player('One')
		player_two = Player('Two')
		deck = Deck()
		deck.shuffler()

		for i in range(26):
			player_one.add_cards(deck.deal_one())
			player_two.add_cards(deck.deal_one())

		self.assertEqual(len(player_one.all_cards), 26)
		self.assertEqual(len(player_two.all_cards), 26)

