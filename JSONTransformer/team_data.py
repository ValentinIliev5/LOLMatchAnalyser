class TeamData(object):
    def __init__(self, first_baron=False, baron_kills=0, first_dragon=False, dragon_kills=0, first_herald=False,
                 herald_kills=0, first_inhibitor=False, inhibitors_killed=0, won=False):
        self.first_baron = first_baron
        self.baron_kills = baron_kills
        self.first_dragon = first_dragon
        self.dragon_kills = dragon_kills
        self.first_herald = first_herald
        self.herald_kills = herald_kills
        self.first_inhibitor = first_inhibitor
        self.inhibitors_killed = inhibitors_killed
        self.won = won
