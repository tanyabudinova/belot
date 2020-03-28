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
def find_max_sequel_announce(announcements):
    return max([x for x in announcements])

def sum_points_with_sequentials(team_announcements):
    return sum([x.points() for x in team_announcements])

def sum_points_without_sequentials(team_announcements):
    return sum([x.points() for x in team_announcements if not x.is_sequential()])

def sum_up_points(team_one_announcements, team_two_announcements):
    if find_max_sequel_announce(team_one_announcements) > find_max_sequel_announce(team_two_announcements):
        return (sum_points_with_sequentials(team_one_announcements), sum_points_without_sequentials(team_two_announcements))
    elif find_max_sequel_announce(team_two_announcements) > find_max_sequel_announce(team_one_announcements):
        return (sum_points_without_sequentials(team_one_announcements), sum_points_with_sequentials(team_two_announcements))
    return (sum_points_without_sequentials(team_one_announcements), sum_points_without_sequentials(team_two_announcements))



