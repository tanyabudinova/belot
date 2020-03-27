from suits import Suit
from ranks import Rank
from card import Card
from announcements import *

def has_belote_in_hand(mode, hand):
    king = Card(Rank.King, Suit(mode))
    queen =Card(Rank.Queen, Suit(mode))
    if king in hand and queen in hand:
        return Announcement(Announcement_Type.Belote,None)