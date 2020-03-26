import unittest
from suits import Suit
class TestSuits(unittest.TestCase):
	def test_returns_true_if_clubs_lesser_than_hearts(self):
		#ASSERT
		clubs = Suit(1)
		hearts = Suit(3)

		#ACT
		result = clubs < hearts

		#ASSERT
		self.assertTrue(result)

	def test_returns_specific_string_for_each_suite(self):
		#ASSERT
		diamonds = Suit(2)
		
		#ACT
		result = str(diamonds)

		#ASSERT
		self.assertEqual(result, 'd')

if __name__ == '__main__':
	unittest.main()