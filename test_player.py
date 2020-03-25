import unittest
from player import Player
from announcements import Announcement
from card import Card
from suits import Suit
from ranks import Rank

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

    def test_announce_with_belot(self):
        pass

    def test_announce_with_cosecutive_cards(self):
        pass

    def test_announce_with_carre(self):
        pass

    def test_announce_with_more_announcements(self):
        pass
    
if __name__ == '__main__':
    unittest.main()