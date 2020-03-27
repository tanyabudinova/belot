from enum import Enum

class Mode(Enum):
    Clubs      = 1
    Diamonds   = 2 
    Hearts     = 3
    Spades     = 4
    All_Trumps = 5
    No_Trumps  = 6

    def __str__(self):
        return self.name.replace('_',' ')