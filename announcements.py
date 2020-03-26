class Belot():
	points = 20
	def __str__(self):
		return "belot"

class Carre():
	def __init__(self, rank):
		if rank.value in range(10, 14):
			self.points = 100
		elif rank.value == 14:
			self.points = 200
		else:
			self.points = 150
		self.rank = rank

	def __str__(self):
		return f"carre of {self.rank}'s"

class SequelCombination():
	def __init__(self, combination):
		self.combination = combination
		if(len(combination) == 3):
			self.points = 20
		elif(len(combination) == 4):
			self.points = 50
		else:
			self.points = 100

	def __str__(self):
		if self.points == 20:
			return "tierce"
		if self.points == 50:
			return "quarte"
		return "quinte"

	def get_highest_card(self):
		return self.combination[-1]

	def __gt__(self, other):
		if self.points == other.points:
			return self.get_highest_card() > other.get_highest_card()
		return self.points > other.points


