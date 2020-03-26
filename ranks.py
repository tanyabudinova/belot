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
        if self.value in range(7, 10):
            return str(self.value)
        if self.value == 11:
            return 'J'
        if self.value == 12:
            return 'Q'
        if self.value == 13:
            return 'K'
        return 'A'
