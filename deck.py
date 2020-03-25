from ranks import Rank
from suits import Suit
from card import Card
class Deck():
    def __init__(self):
        cards = []
        for suit in Suit:
            for rank in Rank:
                cards.append(Card(rank, suit))
        self.cards = cards
