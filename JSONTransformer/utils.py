from player_data import PlayerData
from team_data import TeamData
from iteration_utilities import deepflatten


def get_pings(participant):
    blue_pings, red_pings = 0, 0
    for value in participant:
        if "pings" in value.lower():
            if participant["teamId"] == 100:
                blue_pings += participant[value]
            else:
                red_pings += participant[value]
    return blue_pings, red_pings


def get_player_data(participant):
    player_data = PlayerData()
    player_data.kills = participant["kills"]
    player_data.deaths = participant["deaths"]
    player_data.assists = participant["assists"]
    player_data.champ_experience = participant["champExperience"]
    player_data.damage_to_objectives = participant["damageDealtToObjectives"]
    player_data.gold_spent = participant["goldSpent"]
    player_data.longest_time_spent_living = participant["longestTimeSpentLiving"]
    player_data.pentakills = participant["pentaKills"]
    player_data.total_damage_dealt = participant["totalDamageDealt"]
    player_data.total_damage_to_champions = participant["totalDamageDealtToChampions"]
    player_data.total_shielded_on_teammates = participant["totalDamageShieldedOnTeammates"]
    player_data.total_healed_on_teammates = participant["totalHealsOnTeammates"]
    player_data.total_minions_killed = participant["totalMinionsKilled"]
    player_data.total_time_spent_dead = participant["totalTimeSpentDead"]
    player_data.turret_kills = participant["turretTakedowns"]
    player_data.wards_killed = participant["wardsKilled"]
    player_data.wards_placed = participant["wardsPlaced"]

    return player_data


def join_line_for_csv(player_scores, team_scores, red_pings, blue_pings):
    line = []
    roles = ["TOP", "JUNGLE", "MIDDLE", "BOTTOM", "UTILITY"]
    team_colors = ["red", "blue"]
    for color in team_colors:
        for role in roles:
            player = player_scores[color][role]
            player_data_list = [getattr(player, prop) for prop in vars(player)]
            line.append(player_data_list)

    i = 0
    for color in team_colors:
        team = team_scores[color]
        pings = blue_pings if i == 0 else red_pings
        line.append([pings,
                     team.first_baron,
                     team.baron_kills,
                     team.first_dragon,
                     team.dragon_kills,
                     team.first_herald,
                     team.herald_kills,
                     team.first_inhibitor,
                     team.inhibitors_killed,
                     team.won])
        i += 1
    return list(deepflatten(line))


def get_team_data(team):
    team_data = TeamData()
    team_data.first_baron = team["objectives"]["baron"]["first"]
    team_data.baron_kills = team["objectives"]["baron"]["kills"]
    team_data.first_dragon = team["objectives"]["dragon"]["first"]
    team_data.dragon_kills = team["objectives"]["dragon"]["kills"]
    team_data.first_herald = team["objectives"]["riftHerald"]["first"]
    team_data.herald_kills = team["objectives"]["riftHerald"]["kills"]
    team_data.first_inhibitor = team["objectives"]["inhibitor"]["first"]
    team_data.inhibitors_killed = team["objectives"]["inhibitor"]["kills"]
    team_data.won = team["win"]
    return team_data


def get_fields():
    fields = ("blue_top_kills", "blue_top_deaths", "blue_top_assists", "blue_top_champ_experience",
              "blue_top_damage_to_objectives", "blue_top_gold_spent", "blue_top_longest_time_spent_living",
              "blue_top_pentaKills", "blue_top_damage_dealt", "blue_top_damage_to_champions",
              "blue_top_shielded", "blue_top_healed", "blue_top_minions_killed", "blue_top_time_spent_dead",
              "blue_top_turret_kills", "blue_top_wards_killed", "blue_top_wards_placed",

              "blue_jungle_kills", "blue_jungle_deaths", "blue_jungle_assists", "blue_jungle_champ_experience",
              "blue_jungle_damage_to_objectives", "blue_jungle_gold_spent", "blue_jungle_longest_time_spent_living",
              "blue_jungle_pentaKills", "blue_jungle_damage_dealt", "blue_jungle_damage_to_champions",
              "blue_jungle_shielded", "blue_jungle_healed", "blue_jungle_minions_killed", "blue_jungle_time_spent_dead",
              "blue_jungle_turret_kills", "blue_jungle_wards_killed", "blue_jungle_wards_placed",

              "blue_middle_kills", "blue_middle_deaths", "blue_middle_assists",
              "blue_middle_champ_experience", "blue_middle_damage_to_objectives",
              "blue_middle_gold_spent", "blue_middle_longest_time_spent_living",
              "blue_middle_pentaKills", "blue_middle_damage_dealt", "blue_middle_damage_to_champions",
              "blue_middle_shielded", "blue_middle_healed", "blue_middle_minions_killed",
              "blue_middle_time_spent_dead", "blue_middle_turret_kills", "blue_middle_wards_killed",
              "blue_middle_wards_placed",

              "blue_bot_kills", "blue_bot_deaths", "blue_bot_assists", "blue_bot_champ_experience",
              "blue_bot_damage_to_objectives", "blue_bot_gold_spent", "blue_bot_longest_time_spent_living",
              "blue_bot_pentaKills", "blue_bot_damage_dealt", "blue_bot_damage_to_champions", "blue_bot_shielded",
              "blue_bot_healed", "blue_bot_minions_killed", "blue_bot_time_spent_dead",
              "blue_bot_turret_kills", "blue_bot_wards_killed", "blue_bot_wards_placed",

              "blue_utility_kills", "blue_utility_deaths", "blue_utility_assists", "blue_utility_champ_experience",
              "blue_utility_damage_to_objectives", "blue_utility_gold_spent", "blue_utility_longest_time_spent_living",
              "blue_utility_pentaKills", "blue_utility_damage_dealt",
              "blue_utility_damage_to_champions", "blue_utility_shielded", "blue_utility_healed",
              "blue_utility_minions_killed", "blue_utility_time_spent_dead", "blue_utility_turret_kills",
              "blue_utility_wards_killed", "blue_utility_wards_placed",

              "red_top_kills", "red_top_deaths", "red_top_assists", "red_top_champ_experience",
              "red_top_damage_to_objectives", "red_top_gold_spent", "red_top_longest_time_spent_living",
              "red_top_pentaKills", "red_top_damage_dealt", "red_top_damage_to_champions", "red_top_shielded",
              "red_top_healed", "red_top_minions_killed", "red_top_time_spent_dead", "red_top_turret_kills",
              "red_top_wards_killed", "red_top_wards_placed",

              "red_jungle_kills", "red_jungle_deaths", "red_jungle_assists", "red_jungle_champ_experience",
              "red_jungle_damage_to_objectives", "red_jungle_gold_spent", "red_jungle_longest_time_spent_living",
              "red_jungle_pentaKills", "red_jungle_damage_dealt", "red_jungle_damage_to_champions", "red_jungle_shielded",
              "red_jungle_healed", "red_jungle_minions_killed", "red_jungle_time_spent_dead", "red_jungle_turret_kills",
              "red_jungle_wards_killed", "red_jungle_wards_placed",

              "red_middle_kills", "red_middle_deaths", "red_middle_assists", "red_middle_champ_experience",
              "red_middle_damage_to_objectives", "red_middle_gold_spent", "red_middle_longest_time_spent_living",
              "red_middle_pentaKills", "red_middle_damage_dealt", "red_middle_damage_to_champions", "red_middle_shielded",
              "red_middle_healed", "red_middle_minions_killed", "red_middle_time_spent_dead", "red_middle_turret_kills",
              "red_middle_wards_killed", "red_middle_wards_placed",

              "red_bot_kills", "red_bot_deaths", "red_bot_assists", "red_bot_champ_experience",
              "red_bot_damage_to_objectives", "red_bot_gold_spent", "red_bot_longest_time_spent_living",
              "red_bot_pentaKills", "red_bot_damage_dealt", "red_bot_damage_to_champions", "red_bot_shielded",
              "red_bot_healed", "red_bot_minions_killed", "red_bot_time_spent_dead", "red_bottom_turret_kills",
              "red_bot_wards_killed", "red_bot_wards_placed",

              "red_utility_kills", "red_utility_deaths", "red_utility_assists", "red_utility_champ_experience",
              "red_utility_damage_to_objectives", "red_utility_gold_spent", "red_utility_longest_time_spent_living",
              "red_utility_pentaKills", "red_utility_damage_dealt", "red_utility_damage_to_champions",
              "red_utility_shielded", "red_utility_healed", "red_utility_minions_killed", "red_utility_time_spent_dead",
              "red_utility_turret_kills", "red_utility_wards_killed", "red_utility_wards_placed",

              "blue_pings", "blue_first_baron", "blue_baron_kills", "blue_first_dragon", "blue_dragon_kills",
              "blue_first_herald", "blue_herald_kills", "blue_first_inhibitor", "blue_inhibitor_kills", "blue_victory",

              "red_pings", "red_first_baron", "red_baron_kills", "red_first_dragon", "red_dragon_kills", "red_first_herald",
              "red_herald_kills", "red_first_inhibitor", "red_inhibitor_kills", "red_victory")

    return fields
