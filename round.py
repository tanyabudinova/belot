from deck import Deck
from modes import Mode
from random import choice
from utils import sum_up_points

class Round():
	def __init__(self, team_one, team_two):
		self.team_one = team_one
		self.team_two = team_two
		self.team_one_points = 0
		self.team_two_points = 0
		self.deck = Deck()
		self.mode = choice(list(Mode))

	def draw_cards(self):
		hand = []
		for i in range(8):
			card = self.deck.draw_random_card()
			hand.append(card)
		return hand

	def round_actions(self):
		if self.mode == Mode.No_Trumps:
			self.team_one_points, self.team_two_points = (0, 0)
		else:
			team_one_announcements = self.team_one.announce(self.mode, self.draw_cards(), self.draw_cards())
			team_two_announcements = self.team_two.announce(self.mode, self.draw_cards(), self.draw_cards())
			self.team_one_points, self.team_two_points = sum_up_points(team_one_announcements, team_two_announcements)

	def count_points_of_announcements(self):
		pass

	def get_team_one_points(self):
		return self.team_one_points

	def get_team_two_points(self):
		return self.team_two_points


