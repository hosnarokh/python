import random


class Person:
    def __init__(self, name):
        self.name = name


class Player(Person):
    def __int__(self, name):
        super().__init__(name)


class Team(Person):
    def __init__(self, name):

        super().__init__(name)
        self.players = []

    def add_players(self, player):
        if len(self.players) > 12:
            raise ValueError
        self.players.append(player)

    def players_name(self):
        player_names = []
        for player in self.players:
            player_names.append(player.name)
        return player_names


def main():
    names = ['حسین', 'مازیار', 'اکبر', 'نیما', ' مهدی', 'فرهاد', 'محمد', 'خشایار', 'میلاد', 'مصطفی', 'امین', 'سعید',
             'پویا', 'پوریا', 'رضا', 'علی', 'بهزاد', 'سهیل', 'بهروز', 'شهروز', 'سامان', 'محسن']
    team_a = Team('A')
    team_b = Team('B')
    for team in [team_a, team_b]:
        for i in range(11):
            rand_idx = random.randrange(len(names))
            random_name = names[rand_idx]
            player = Player(random_name)
            team.add_players(player)
            names.pop(rand_idx)

        random_names = names

    print(team_a.players_name())
    print(team_b.players_name())


main()



"""chat gbt
import random

class Human:
    def __init__(self, name):
        self.name = name

class Footballer(Human):
    def __init__(self, name):
        super().__init__(name)

players = ["حسین", "مازیار", "اکبر", "نیما", "مهدی", "فرهاد", "محمد", "خشایار",
           "میلاد", "مصطفی", "امین", "سعید", "پویا", "پوریا", "رضا", "علی",
           "بهزاد", "سهیل", "بهروز", "شهروز", "سامان", "محسن"]

team_a = []
team_b = []

random.shuffle(players)

for i in range(11):
    team_a.append(Footballer(players.pop()))

for player in players:
    team_b.append(Footballer(player))

for player in team_a:
    print(f"{player.name} - تیم A")

for player in team_b:
    print(f"{player.name} - تیم B")
"""
