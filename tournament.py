from round import Round
from team import Team
from texttable import Texttable

class Tournament:
    def __init__(self):
        self.rounds = []
        self.games = []

    def initialize(self):
        team_one_name = input("Enter Team 1 name:")
        team_two_name = input("Enter Team 2 name:")

        team_one_players = input(f"{team_one_name} players:")
        team_one_players.split(", ")
        team_one_player_one = team_one_players[0]
        team_one_player_two = team_one_players[1]
        self.team_one = Team(team_one_name, team_one_player_one, team_one_player_two)

        team_two_players = input(f"{team_two_name} players:")
        team_two_players.split(", ")
        team_two_player_one = team_two_players[0]
        team_two_player_two = team_two_players[1]
        self.team_two = Team(team_two_name, team_two_player_one, team_two_player_two)

        self.divider_length = len(team_one_name) + len(team_two_name) + 21

    def generate_round(self):
        new_round = Round(self.team_one, self.team_two)
        new_round.round_actions()
        self.rounds.append(new_round)

    def to_txt_file(self, rounds,file, print_header): 
        table = Texttable()
        table.set_cols_width([len(self.team_one.get_name()) + 9, len(self.team_two.get_name()) + 9])
        if print_header:
            deco = Texttable.HEADER | Texttable.VLINES
            table.header([self.team_one.get_name(), self.team_two.get_name()])
        else:
            deco = Texttable.VLINES
        table.set_deco(deco)
        table.set_chars(['-', '|', '=', '='])
        rows = [[str(rounds[0].get_team_one_points()),str(rounds[0].get_team_two_points())]]
        for i in range(1,len(rounds)):
            column1 = f"{sum([x.get_team_one_points() for x in rounds[:i]])} + {rounds[i].get_team_one_points()}"
            column2 = f"{sum([x.get_team_two_points() for x in rounds[:i]])} + {rounds[i].get_team_two_points()}"
            rows.append([column1,column2])
        table.add_rows(rows, header = False)
        file.write(table.draw())
        file.write('\n')
        self.write_divider_to_file(file)
        table.reset()
        table.add_row([f"({self.team_one.games_won})", f"({self.team_two.games_won})"])
        table.set_cols_align(["c","c"])        
        file.write(table.draw())
        file.write('\n')
        self.write_divider_to_file(file)

    def to_json_file(self):
        pass

    @staticmethod
    def there_is_winner(rounds):
        team_one_points = sum([x.team_one_points for x in rounds])
        team_two_points = sum([x.team_two_points for x in rounds])

        if (team_one_points <= 150 and team_two_points <= 150) or (team_one_points == team_two_points):
            return 0
        else:
            if team_one_points > team_two_points:
                return 1
            else:
                return 2

    def write_divider_to_file(self, file):
        file.write('=' * self.divider_length)
        file.write('\n')

    def start(self):
        self.initialize()
        with open("results.txt","w") as file:
            first_round = True
            while self.team_one.games_won < 2 and self.team_two.games_won < 2:
                winner = self.there_is_winner(self.rounds) 
                while not winner:
                    self.generate_round()
                    winner = self.there_is_winner(self.rounds)

                self.games.append(self.rounds)
                if winner == 1:
                    self.team_one.game_won()
                else:
                    self.team_two.game_won()
                self.to_txt_file(self.rounds, file, first_round)
                if first_round:
                    first_round = False
                self.rounds.clear()
