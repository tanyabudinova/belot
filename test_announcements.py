import unittest
from announcements import *

class TestAnnouncements(unittest.TestCase):
	def test_sequential_type_bigger_than_others(self):
		tierce = Announcement(Announcement_Type.Tierce, 8)
		quarte = Announcement(Announcement_Type.Quarte, 8)
		quinte = Announcement(Announcement_Type.Quinte, 8)
		belote = Announcement(Announcement_Type.Belote, None)
		carre = Announcement(Announcement_Type.Carre, 8)

		self.assertTrue(tierce > belote)
		self.assertTrue(quarte > belote)
		self.assertTrue(quinte > belote)
		self.assertTrue(tierce > carre)
		self.assertTrue(quarte > carre)
		self.assertTrue(quinte > carre)

	def test_order_between_sequential_types(self):
		tierce = Announcement(Announcement_Type.Tierce, 8)
		quarte = Announcement(Announcement_Type.Quarte, 8)
		quinte = Announcement(Announcement_Type.Quinte, 8)

		self.assertFalse(tierce > quarte)
		self.assertTrue(quinte > tierce)
		self.assertTrue(quinte > quarte)

	def test_order_between_equal_sequential_types_which_start_from_different_cards(self):
		tierce = Announcement(Announcement_Type.Tierce, 8)
		tierce_bigger = Announcement(Announcement_Type.Tierce, 11)
		quarte = Announcement(Announcement_Type.Quarte, 8)
		quarte_bigger = Announcement(Announcement_Type.Quarte, 10)
		quinte = Announcement(Announcement_Type.Quinte, 8)
		quinte_bigger = Announcement(Announcement_Type.Quinte, 12)

		self.assertTrue(tierce_bigger > tierce)
		self.assertTrue(quarte_bigger > quarte)
		self.assertTrue(quinte_bigger > quinte)

# from announcements import Belot, Carre, SequelCombination
# from ranks import Rank
# from card import Card
# class TestBelot(unittest.TestCase):
# 	def test_returns_true_if_points_of_belot_are_twenty(self):
# 		#ARRANGE
# 		belot = Belot()

# 		#ACT
# 		result = belot.points 

# 		#ASSERT
# 		self.assertEqual(result, 20)

# 	def test_returns_true_if_belot_is_casted_to_string_proeprly(self):
# 		#ARRANGE
# 		belot = Belot()

# 		#ACT
# 		result = str(belot)

# 		#ASSERT
# 		self.assertEqual(result, "belot")

# class TestCarre(unittest.TestCase):
# 	def test_returns_points_for_carre_of_face_cards_or_tens(self):
# 		#ARRANGE
# 		rank = Rank(11)
# 		carre = Carre(rank)

# 		#ACT
# 		result = carre.points

# 		#ASSERT
# 		self.assertEqual(result, 100)
# 	def test_returns_points_for_carre_of_aces(self):
# 		#ARRANGE
# 		rank = Rank(14)
# 		carre = Carre(rank)

# 		#ACT
# 		result = carre.points

# 		#ASSERT
# 		self.assertEqual(result, 200)
# 	def test_returns_points_for_carre_of_nines(self):
# 		#ARRANGE
# 		rank = Rank(9)
# 		carre = Carre(rank)

# 		#ACT
# 		result = carre.points

# 		#ASSERT
# 		self.assertEqual(result, 150)
# 	def test_returns_true_if_stirng_cast_of_carre_of_tens_is_correct(self):
# 		#ARRANGE
# 		rank = Rank(10)
# 		carre = Carre(rank)

# 		#ACT
# 		result = str(carre)

# 		#ASSERT
# 		self.assertEqual(result, "carre of 10's")

# 	def test_returns_true_if_stirng_cast_of_carre_of_kings_is_correct(self):
# 		#ARRANGE
# 		rank = Rank(13)
# 		carre = Carre(rank)

# 		#ACT
# 		result = str(carre)

# 		#ASSERT
# 		self.assertEqual(result, "carre of K's")

# class TestSequelCombination(unittest.TestCase):
# 	def test_returns_tierce_if_three_sequel_combination_passed(self):
# 		#ARRANGE
# 		sequel = [Card(7,1), Card(8,1), Card(9, 1)]
# 		combination = SequelCombination(sequel)

# 		#ACT
# 		result = combination.points

# 		#ASSERT
# 		self.assertEqual(result, 20)

# 	def test_returns_quarte_if_four_sequel_combination_passed(self):
# 		#ARRANGE
# 		sequel = [Card(7,1), Card(8,1), Card(9, 1), Card(10,1)]
# 		combination = SequelCombination(sequel)

# 		#ACT
# 		result = combination.points

# 		#ASSERT
# 		self.assertEqual(result, 50)

# 	def test_returns_quarte_if_four_sequel_combination_passed(self):
# 		#ARRANGE
# 		sequel = [Card(7,1), Card(8,1), Card(9, 1), Card(10,1), Card(11,1)]
# 		combination = SequelCombination(sequel)

# 		#ACT
# 		result = combination.points

# 		#ASSERT
# 		self.assertEqual(result, 100)

# 	def test_returns_true_if_correct_string_is_returned_for_tierce(self):
# 		#ARRANGE
# 		sequel = [Card(7,1), Card(8,1), Card(9, 1)]
# 		combination = SequelCombination(sequel)

# 		#ACT
# 		result = str(combination)

# 		#ASSERT
# 		self.assertEqual(result, "7c 8c 9c  - tierce")

# 	def test_returns_true_if_correct_string_is_returned_for_quarte(self):
# 		#ARRANGE
# 		sequel = [Card(7,1), Card(8,1), Card(9, 1), Card(10,1)]
# 		combination = SequelCombination(sequel)

# 		#ACT
# 		result = str(combination)

# 		#ASSERT
# 		self.assertEqual(result, "7c 8c 9c 10c  - quarte")

# 	def test_returns_true_if_correct_string_is_returned_for_quinte(self):
# 		#ARRANGE
# 		sequel = [Card(7,1), Card(8,1), Card(9, 1), Card(10,1), Card(11,1)]
# 		combination = SequelCombination(sequel)

# 		#ACT
# 		result = str(combination)

# 		#ASSERT
# 		self.assertEqual(result, "7c 8c 9c 10c Jc  - quinte")

# 	def test_returns_highest_card_of_the_combination(self):
# 		#ARRANGE
# 		sequel = [Card(7,1), Card(8,1), Card(9, 1), Card(10,1), Card(11,1)]
# 		combination = SequelCombination(sequel)

# 		#ACT
# 		result = combination.get_highest_card()

# 		#ASSERT
# 		self.assertEqual(result, Card(11,1))

# 	def test_returns_true_if_two_combinations_with_same_value_are_compared_correctly(self):
# 		#ARRANGE
# 		sequel_comb_higher = SequelCombination([Card(7,4), Card(8,4), Card(9, 4)])
# 		sequel_comb_lesser = SequelCombination( [Card(7,2), Card(8,2), Card(9, 2)])

# 		#ACT
# 		result = sequel_comb_higher > sequel_comb_lesser

# 		#ASSERT
# 		self.assertTrue(result)

# 	def test_returns_true_if_two_combinations_with_different_value_are_compared_correctly(self):
# 		#ARRANGE
# 		sequel_comb_higher = SequelCombination( [Card(7,2), Card(8,2), Card(9, 2), Card(10, 2)])
# 		sequel_comb_lesser = SequelCombination([Card(7,4), Card(8,4), Card(9, 4)])

# 		#ACT
# 		result = sequel_comb_higher > sequel_comb_lesser

# 		#ASSERT
# 		self.assertTrue(result)




if __name__ == '__main__':
	unittest.main()