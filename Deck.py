from Ranks import Rank
from Suites import Suite
from Card import Card
class Deck():
	def __init__(self):
		cards = []
		for suite in Suite:
			for rank in Rank:
				cards.append(Card(rank, suite))
		self.cards = cards
