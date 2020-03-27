from suits import Suit
from ranks import Rank
from card import Card
from announcements import *

def has_belote_in_hand(mode, hand):
    king = Card(Rank.King, Suit(mode))
    queen =Card(Rank.Queen, Suit(mode))
    if king in hand and queen in hand:
        return Announcement(Announcement_Type.Belote,None)

def group(list):
    if len(list) == 0:
        return []
    curr_group = [list[0]]
    result = []
    for i in range(1,len(list)):
        if list[i] in curr_group:
            curr_group.append(list[i])
        else:
            result.append(curr_group[:])
            curr_group.clear()
            curr_group.append(list[i])
    result.append(curr_group[:])
    return result