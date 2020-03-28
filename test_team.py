import unittest
from card import Card
from modes import Mode
from team import Team
class TestTeam(unittest.TestCase):
	def test_teturs_true_if_method_returns_merged_list_of_announcements(self):
		#ARRANGE
		team = Team("Elephant", "Tony", "Tanya")
		hand_one = [Card(7, 1), Card(8, 1), Card(9, 1), Card(10, 2), Card(11, 3), Card(12, 4), Card(13, 4)]
		hand_two = [Card(7, 2), Card(8, 2), Card(9, 3), Card(10, 3), Card(11, 3), Card(12, 3), Card(13, 3)]
		mode = Mode(4)

		#ACT
		result = [str(x) for x in team.announce(mode, hand_one, hand_two)]


		#ASSERT
		self.assertEqual(result, ["belote", "tierce from 7", "quinte from 9"])

	def test_returns_true_if_name_of_team_printed_correctly(self):
		#ARRANGE
		team = Team("Elephant", "Tony", "Tanya")

		#ACT
		result = str(team)

		#ASSERT
		self.assertEqual(result, "Elephant players: Tony, Tanya")





if __name__ == '__main__':	
	unittest.main()