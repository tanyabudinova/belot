from enum import Enum 
class Rank(Enum):
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
        return str(self.value)
