class PlayerData(object):
    def __init__(self, kills=0, deaths=0, assists=0, champ_experience=0, damage_to_objectives=0,
                 gold_spent=0, longest_time_spent_living=0, pentakills=0, total_damage_dealt=0,
                 total_damage_to_champions=0, total_shielded_on_teammates=0, total_healed_on_teammates=0,
                 total_time_spent_dead=0, total_minions_killed=0, turret_kills=0, wards_killed=0, wards_placed=0):
        self.kills = kills
        self.deaths = deaths
        self.assists = assists
        self.champ_experience = champ_experience
        self.damage_to_objectives = damage_to_objectives
        self.gold_spent = gold_spent
        self.longest_time_spent_living = longest_time_spent_living
        self.pentakills = pentakills
        self.total_damage_dealt = total_damage_dealt
        self.total_damage_to_champions = total_damage_to_champions
        self.total_shielded_on_teammates = total_shielded_on_teammates
        self.total_healed_on_teammates = total_healed_on_teammates
        self.total_minions_killed = total_minions_killed
        self.total_time_spent_dead = total_time_spent_dead
        self.turret_kills = turret_kills
        self.wards_killed = wards_killed
        self.wards_placed = wards_placed
