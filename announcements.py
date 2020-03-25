from enum import Enum

class Announcement(Enum):
    Belote = 1
    Tierce = 2
    Quarte = 3
    Quinte = 4
    Carre  = 5

    def __str__(self):
        return self.name.lower()