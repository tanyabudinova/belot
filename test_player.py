import unittest
from player import Player
from announcements import *
from card import Card
from suits import Suit
from ranks import Rank
from modes import Mode

def string_to_card(card):
    rank = int(card[:-1])
    suit = card[-1]

    rank = Rank(rank)
    #suit = Suit("cdhs".index(suit) + 1)
    if suit == 'c':
        suit = Suit.Clubs
    elif suit == 'd':
        suit = Suit.Diamonds
    elif suit == 'h':
        suit = Suit.Hearts
    elif suit == 's':
        suit = Suit.Spades

    return Card(rank,suit)

def generate_cards(cards):
    return list(map(string_to_card, cards))

class TestPlayer(unittest.TestCase):
    def test_correct_ordering_after_receiving_cards(self):
        cards = generate_cards(["7s", "8s", "9s", "10c", "11d", "12d", "13d", "14s"])
        player = Player("Panda")

        player.receive_cards(cards)
        expected = generate_cards(["10c", "11d", "12d", "13d", "7s", "8s", "9s", "14s"])

        self.assertEqual(expected, player.get_hand())

    def test_announce_with_belot_when_in_the_correct_suit_mode(self):
        cards = generate_cards(["7s", "8s", "9s", "10c", "11d", "12d", "13d", "14s"])
        player = Player("Panda")

        player.receive_cards(cards)
        result = player.announce(Mode.Diamonds)

        self.assertEqual([Announcement(Announcement_Type.Belote,None)], result)

    def test_announce_with_belot_when_not_in_the_correct_suit_mode(self):
        cards = generate_cards(["7s", "8s", "9s", "10c", "11d", "12d", "13d", "14s"])
        player = Player("Panda")

        player.receive_cards(cards)
        result = player.announce(Mode.Spades)

        self.assertEqual([], result)

    def test_announce_with_belot_when_in_all_trumps_mode(self):
        cards_with_belot = generate_cards(["7s", "8s", "9s", "12c", "13c", "12d", "13d", "14s"])
        cards_without_belot = generate_cards(["7s", "8s", "9s", "12c", "14c", "12d", "13s", "14s"])
        player = Player("Panda")

        player.receive_cards(cards_with_belot)
        result = player.announce(Mode.All_Trumps)
        player.receive_cards(cards_without_belot)
        result2 = player.announce(Mode.All_Trumps)

        self.assertEqual([Announcement(Announcement_Type.Belote,None)], result)
        self.assertEqual([], result2)

    def test_announce_with_cosecutive_cards(self):
        # cards_tierce = generate_cards(["7s", "8s", "9s", "10c", "13c", "12d", "13d", "14s"])
        # player = Player("Panda")

        # player.receive_cards(cards_quarte)
        # result = player.announce(Mode.All_Trumps)

        # self.assertEqual([Announcement(Announcement_Type.Quarte,7)], result)
        pass

    def test_announce_with_carre(self):
        cards_no_carre = generate_cards(["7s", "8s", "9s", "7c", "7d", "12d", "13d", "7h"])
        cards_carre = generate_cards(["7s", "8s", "9s", "9c", "9d", "12d", "13d", "9h"])
        player = Player("Panda")
        
        player.receive_cards(cards_no_carre)
        result = player.announce(Mode.Spades)
        player.receive_cards(cards_carre)
        result2 = player.announce(Mode.Spades)

        self.assertEqual([], result)
        self.assertEqual([Announcement(Announcement_Type.Carre,9)], result2)

    def test_announce_with_more_announcements(self):
        pass
    
if __name__ == '__main__':
    unittest.main()