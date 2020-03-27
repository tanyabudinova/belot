from announcements import *
from operator import attrgetter
from modes import Mode
from ranks import Rank
from suits import Suit
from utils import has_belote_in_hand

class Player:
    def __init__(self, name):
        self.name = name
        self.__hand = []

    def __order_cards(self):
        self.__hand.sort(key = attrgetter("rank"))
        self.__hand.sort(key = attrgetter("suit"))

    def get_hand(self):
        return self.__hand
        
    def receive_cards(self, hand):
        self.__hand = hand
        self.__order_cards()

    def announce(self, mode):
        announcement = []
        announcement.append(self.__has_belote(mode))
        announcement.append(self.__has_carre())
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
        ranks =[Rank.Nine, Rank.Ten, Rank.Jack, Rank.Queen, Rank.King, Rank.Ace]
        for i in ranks:
            if hand_ranks.count(i) == 4:
                return Announcement(Announcement_Type.Carre,i.value)

    def __has_consecutive_cards(self):
        pass