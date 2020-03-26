import unittest
from card import Card 

class TestCard(unittest.TestCase):
	def test_returns_true_if_cards_of_the_same_suite_are_compared_correctly(self):
		#ARRANGE
		card_one = Card(11, 1)
		card_two = Card(12, 1)

		#ACT
		result = card_one < card_two

		#ASSERT
		self.assertTrue(result)

	def test_returns_true_if_cards_of_different_suite_are_compared_correctly(self):
		#ARRAANGE
		card_one = Card(13, 2)
		card_two = Card(8, 4)

		#ACT
		result = card_one < card_two

		#ASSERT
		self.assertTrue(result)

	def test_returns_true_if_card_as_number_is_printed_correctly(self):
		#AEEANGE
		card = Card(10, 2)

		#ACT
		result = str(card)

		#ASSERT
		self.assertEqual(result, "10d")

	def test_returns_true_if_card_as__is_printed_correctly(self):
		#AEEANGE
		card = Card(13, 4)

		#ACT
		result = str(card)

		#ASSERT
		self.assertEqual(result, "Ks")

if __name__ == '__main__':
	unittest.main()