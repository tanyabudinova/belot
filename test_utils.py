import unittest
from utils import *
from announcements import *
class TestSumUpPoints(unittest.TestCase):
	def test_returns_correct_points_with_sequential(self):
		#ARRANGE
		announcements = [Announcement(Announcement_Type(1), ''), Announcement(Announcement_Type(3), ''), Announcement(Announcement_Type(2), '')]
		
		#ACT
		result = sum_points_with_sequentials(announcements)

		#ASSERT
		self.assertEqual(result, 240)
	def test_returns_correct_points_for_sequential(self):
		#ARRANGE
		announcements = [Announcement(Announcement_Type(1), ''), Announcement(Announcement_Type(3), ''), Announcement(Announcement_Type(2), '')]
		
		#ACT
		result = sum_points_without_sequentials(announcements)

		#ASSERT
		self.assertEqual(result, 220)

	def test_returns_tuple_of_points_of_the_first_and_the_second_team(self):
		#ARRANGE
		announcements_team_one = [Announcement(Announcement_Type(3), 3), Announcement(Announcement_Type(1), None), Announcement(Announcement_Type(2), 9)]
		announcements_team_two = [Announcement(Announcement_Type(1), None), Announcement(Announcement_Type(5), 3), Announcement(Announcement_Type(3), 3)]

		#ACT
		result = sum_up_points(announcements_team_one, announcements_team_two)

		#ASSERT
		self.assertEqual(result, (220, 140))

	def test(self):
		announcements_team_one = [Announcement(Announcement_Type(3), 3), Announcement(Announcement_Type(1), None), Announcement(Announcement_Type(2), 9)]
		announcements_team_two = [Announcement(Announcement_Type(1), None), Announcement(Announcement_Type(5), 3), Announcement(Announcement_Type(3), 3)]
		result = find_max_sequel_announce(announcements_team_two) > find_max_sequel_announce(announcements_team_one)

		self.assertTrue(result)



if __name__ == '__main__':
	unittest.main()
