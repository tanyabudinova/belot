from suits import Suit
from ranks import Rank
from card import Card
from announcements import *

def has_belote_in_hand(mode, hand):
    king = Card(Rank.King, Suit(mode))
    queen = Card(Rank.Queen, Suit(mode))
    if king in hand and queen in hand:
        return Announcement(Announcement_Type.Belote,None)

def find_max_sequel_announce(announcements):
    return max(announcements)

def sum_points_with_sequentials(team_announcements):
    return sum([x.points() for x in team_announcements])

def sum_points_without_sequentials(team_announcements):
    return sum([x.points() for x in team_announcements if not x.is_sequential()])

def sum_up_points(team_one_announcements, team_two_announcements):
    if team_one_announcements == [] or team_two_announcements == []:
        return (sum_points_with_sequentials(team_one_announcements), sum_points_with_sequentials(team_two_announcements))
    if find_max_sequel_announce(team_one_announcements) > find_max_sequel_announce(team_two_announcements):
    #if max(team_one_announcements) > max(team_two_announcments):
        return (sum_points_with_sequentials(team_one_announcements), sum_points_without_sequentials(team_two_announcements))
    elif find_max_sequel_announce(team_two_announcements) > find_max_sequel_announce(team_one_announcements):
        return (sum_points_without_sequentials(team_one_announcements), sum_points_with_sequentials(team_two_announcements))
    return (sum_points_without_sequentials(team_one_announcements), sum_points_without_sequentials(team_two_announcements))

