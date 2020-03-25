class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __eq__(self, other):
        return (self.rank, self.suit) == (other.rank, other.suit)

    def __str__(self):
        str_suit = self.suit.name.lower()[0]
        return f"{self.rank}{str_suit}"