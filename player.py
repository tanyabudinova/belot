from announcements import Announcement
from card import Card
from operator import attrgetter

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
        pass

    def __has_belot(self, mode):
        pass

    def __has_carre(self):
        pass

    def __has_consecutive_cards(self):
        pass