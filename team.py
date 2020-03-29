from player import Player 

class Team():
	def __init__(self, name, name_one, name_two):
		self.name = name
		self.player_one = Player(name_one)
		self.player_two = Player(name_two)
		self.team_announcements = []
		self.games_won = 0

	def announce(self, mode, hand_one, hand_two):
			return self.player_one.player_actions(hand_one, mode) + self.player_two.player_actions(hand_two, mode)

	def get_name(self):
		return self.name

	def __str__(self):
		return f"{self.name} players: {self.player_one.get_name()}, {self.player_two.get_name()}"

	def game_won(self):
		self.games_won += 1

		