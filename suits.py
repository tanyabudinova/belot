from enum import Enum 
class Suit(Enum):
    Clubs = 1
    Diamonds = 2
    Hearts = 3
    Spades = 4

    def __gt__(self, other):
        return self.value > other.value
