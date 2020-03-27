# class Belot():
# 	points = 20
# 	def __str__(self):
# 		return "belot"

# class Carre():
# 	def __init__(self, rank):
# 		if rank.value in range(10, 14):
# 			self.points = 100
# 		elif rank.value == 14:
# 			self.points = 200
# 		else:
# 			self.points = 150
# 		self.rank = rank

# 	def __str__(self):
# 		return f"carre of {self.rank}'s"

# class SequelCombination():
# 	def __init__(self, combination):
# 		self.combination = combination
# 		if(len(combination) == 3):
# 			self.points = 20
# 		elif(len(combination) == 4):
# 			self.points = 50
# 		else:
# 			self.points = 100

# 	def __str__(self):
# 		text = ''.join([str(x) + ' ' for x in self.combination])
# 		if self.points == 20:
# 			return f"{text} - tierce"
# 		if self.points == 50:
# 			return f"{text} - quarte"
# 		return f"{text} - quinte"

# 	def get_highest_card(self):
# 		return self.combination[-1]

# 	def __gt__(self, other):
# 		if self.points == other.points:
# 			return self.get_highest_card() > other.get_highest_card()
# 		return self.points > other.points

# <<<<<<< Updated upstreamf

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

class Announcement:
    def __init__(self, a_type, info):
        self.__a_type = a_type
        self.__info = info

    def __str__(self):
        if self.__a_type == Announcement_Type.Belote:
            return srt(self.type)
        elif self.__a_type == Announcement_Type.Carre:
            return srt(self.type) + "of " + str(self.__info) + 's'
        else:
            return str(self.type) + "from" + str(self.__info)

    def __eq__(self, other):
        return (self.__a_type, self.__info) == (other.__a_type, other.__info)

    def __gt__(self, other):
        if self.__a_type.is_sequential() and other.__a_type.is_sequential():
            if self.__a_type == other.__a_type:
                return self.__info > other.__info
        else:
            return self.__a_type > other.__a_type
