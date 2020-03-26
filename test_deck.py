import unittest
from deck import Deck
from card import Card

class TestDeck(unittest.TestCase):
	def test_returns_true_if_all_elements_are_cards(self):
		#ARRANGE
		deck = Deck()

		#ACT
		result = all([isinstance(x, Card) for x in deck.cards])

		#ASSERT
		self.assertTrue(result)

	def test_returns_true_if_each_card_is_lesser_than_the_next_one_so_there_are_not_repeated_cards(self):
		#ARRANGE
		deck = Deck()

		#ACT
		result = True
		for i in range(0, len(deck.cards) - 1):
			if not deck.cards[i] < deck.cards[i + 1]:
				result = False

		#ASSERT
		self.assertTrue(result)



if __name__ == '__main__':
	unittest.main()