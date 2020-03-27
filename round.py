from deck import Deck
from modes import Mode
import random

class Round():
	def __init__(self, team_one, team_two):
		self.team_one = team_one
		self.team_two = team_two
		self.deck = Deck()
		self.mode = random.choice(Mode)

	#това май може да се отдели като utulk-а, но не съм сигурен
	def draw_seven_cards(self):
		hand = []
		for i in range(7):
			random = random.choice(self.deck)
			self.deck.remove(random)
			hand.append(random)
		return hand

	def round_actions(self):
		team_one_announcements = team_one.announce(self.mode, draw_seven_cards(), draw_seven_cards())
		team_two_announcement = team_two.announce(self.mode, draw_seven_cards(), draw_seven_cards())

	def count_points_of_announcements(self):
		pass




