from ranks import Rank
from suites import Suite
from card import Card
class Deck():
	def __init__(self):
		cards = []
		for suite in Suite:
			for rank in Rank:
				cards.append(Card(rank, suite))
		self.cards = cards
