from ranks import Rank
from suits import Suit
from card import Card
from random import choice

class Deck():
    def __init__(self):
        cards = []
        for suit in Suit:
            for rank in Rank:
                cards.append(Card(rank, suit))
        self.cards = cards

    def draw_random_card(self):
        card = choice(self.cards)
        self.cards.remove(card)
        return card