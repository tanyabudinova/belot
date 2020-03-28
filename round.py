from deck import Deck
from modes import Mode
import random

class Round():
	def __init__(self, team_one, team_two):
		self.team_one = team_one
		self.team_two = team_two
		self.deck = Deck()
		self.mode = random.choice(Mode)

	def draw_seven_cards(self):
		hand = []
		for i in range(7):
			random = random.choice(self.deck)
			self.deck.remove(random)
			hand.append(random)
		return hand

	def round_actions(self):
		team_one_announcements = team_one.announce(self.mode, self.draw_seven_cards(), self.draw_seven_cards())
		team_two_announcements = team_two.announce(self.mode, self.draw_seven_cards(), self.draw_seven_cards())
		return sum_up_points(team_one_announcement, team_two_announcements)

	def count_points_of_announcements(self):
		pass




