from announcements import *
from operator import attrgetter
from modes import Mode
from ranks import Rank
from suits import Suit
from utils import has_belote_in_hand
from itertools import groupby

class Player:
    def __init__(self, name):
        self.name = name
        self.__hand = []

    def __order_cards(self):
        self.__hand.sort()

    def get_hand(self):
        return self.__hand
        
    def receive_cards(self, hand):
        self.__hand = hand
        self.__order_cards()

    def announce(self, mode):
        announcement = []
        announcement.append(self.__has_belote(mode))
        announcement.append(self.__has_carre())
        announcement.extend(self.__has_consecutive_cards())
        return list(filter(None,announcement))

    def __has_belote(self, mode):
        if mode != Mode.All_Trumps:
            return has_belote_in_hand(mode.value, self.__hand)
        else:
            for i in range(1,5):
                belote = has_belote_in_hand(i, self.__hand)
                if belote:
                    return belote

    def __has_carre(self):
        hand_ranks = list(map(attrgetter("rank"), self.__hand))
        ranks = [Rank.Nine, Rank.Ten, Rank.Jack, Rank.Queen, Rank.King, Rank.Ace]
        for i in ranks:
            if hand_ranks.count(i) == 4:
                return Announcement(Announcement_Type.Carre,i.value)

    def __has_consecutive_cards(self):
        result = []
        grouped_hand = [list(g) for _, g in groupby(self.__hand, key = attrgetter("suit"))]
        grouped_hand = (list(map(lambda y: list(map(lambda x: x.rank, y)),grouped_hand)))
        for group in grouped_hand:
            l = []
            for i in range(len(group) - 1):
                l.append(group[i + 1] - group[i])
            l = [list(g) for _, g in groupby(l)]
            for i in range(len(l)):
                if l[i][0] == 1:
                    idx = sum(list(map(len,l[:i])))
                    if len(l[i]) == 2:
                        result.append(Announcement(Announcement_Type.Tierce, group[idx]))
                    if len(l[i]) == 3:
                        result.append(Announcement(Announcement_Type.Quarte, group[idx]))
                    if len(l[i]) >= 4:
                        result.append(Announcement(Announcement_Type.Quinte, group[idx]))
        return result

    def player_actions(self, hand, mode):
            self.receive_cards(hand)
            return self.announce(mode)

    def get_name(self):
            return self.name

        

            
