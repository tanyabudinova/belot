from ranks import Rank 
from suits import Suit

class Card():
    def __init__(self, rank, suit):
        self.rank = Rank(rank)
        self.suit = Suit(suit)

    def __gt__(self, other):
    	if self.suit == other.suit:
    		return self.rank > other.rank
    	return self.suit > other.suit

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __eq__(self, other):
    	return self.suit == other.suit and self.rank == other.rank