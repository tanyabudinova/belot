from enum import Enum 
class Suit(Enum):
    Clubs = 1
    Diamonds = 2
    Hearts = 3
    Spades = 4

    def __gt__(self, other):
        return self.value > other.value

    def __str__(self):
    	if self.value == 1:
    		return 'c'
    	elif self.value == 2:
    		return 'd'
    	elif self.value == 3:
    		return 'h'
    	else:
    		return 's'
