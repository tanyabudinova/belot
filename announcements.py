from enum import Enum

class Announcement_Type(Enum):
    Belote = 1
    Carre  = 2
    Tierce = 3
    Quarte = 4
    Quinte = 5

    def __str__(self):
        return self.name.lower()

    def is_sequential(self):
        return self.value >= Announcement_Type.Tierce.value

    def __gt__(self, other):
        return self.value > other.value

class Announcement:
    def __init__(self, a_type, info):
        self.__a_type = a_type
        self.__info = info

    def __str__(self):
        if self.__a_type == Announcement_Type.Belote:
            return str(self.__a_type)
        elif self.__a_type == Announcement_Type.Carre:
            return str(self.__a_type) + " of " + str(self.__info) + 's'
        else:
            return str(self.__a_type) + " from " + str(self.__info)

    def __eq__(self, other):
        return (self.__a_type, self.__info) == (other.__a_type, other.__info)

    def __gt__(self, other):
        if self.__a_type.is_sequential() and other.__a_type.is_sequential():
            if self.__a_type == other.__a_type:
                return self.__info > other.__info
        return self.__a_type > other.__a_type

    def is_sequential(self):
        return self.__a_type.is_sequential()

    def points(self):
        if self.__a_type.name == 'Belote':
            return 20
        elif self.__a_type.name == 'Tierce':
            return 20
        elif self.__a_type.name == 'Quarte':
            return 50
        elif self.__a_type.name == 'Quinte':
            return 100
        elif self.__a_type.name == 'Carre':
            return 200
