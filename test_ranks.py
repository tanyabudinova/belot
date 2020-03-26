import unittest
from ranks import Rank

class TestRanks(unittest.TestCase):
	def test_returns_true_if_jack_lesser_than_ace(self):
		#ARRANGE
		jack = Rank(11)
		ace = Rank(14)

		#ACT
		result = jack < ace

		#ASSERT
		self.assertTrue(result)

	def test_returns_specific_string_for_each_rank(self):
		#ARRANGE
		queen = Rank(12)

		#ACT
		result = str(queen)

		#ASSERT
		self.assertEqual(result, 'Q')

if __name__ == '__main__':
	unittest.main()