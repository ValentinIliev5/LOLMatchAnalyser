import ujson
import utils
from player_data import PlayerData
from team_data import TeamData

dataF = open('cleanedData.json')
full_data = ujson.load(dataF)

dataF.close()

# teamId: 100 = blue 200 = red

random_game = full_data[3]
info = random_game["info"]
participants = info["participants"]
teams = info["teams"]

game_duration = info["gameDuration"]
queue_id = info["queueId"]

player_scores = {"blue": {}, "red": {}}

blue_pings, red_pings = 0, 0

for participant in participants:
    b, r = utils.get_pings(participant)
    blue_pings += b
    red_pings += r

    team_color = "blue" if participant["teamId"] == 100 else "red"

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

    player_dict = {participant["teamPosition"]: player_data}

    player_scores[team_color][participant["teamPosition"]] = player_data

# print(player_scores["red"]["MIDDLE"].wards_killed)
team_scores = {"blue": {}, "red": {}}

for team in teams:
    team_color = "blue" if team["teamId"] == 100 else "red"
    print(team["objectives"])
    team_data = TeamData()

    team_data.first_baron = team["objectives"]["baron"]["first"]
    team_data.baron_kills = team["objectives"]["baron"]["kills"]
    team_data.first_dragon = team["objectives"]["dragon"]["first"]
    team_data.dragon_kills = team["objectives"]["dragon"]["kills"]
    team_data.first_inhibitor = team["objectives"]["inhibitor"]["first"]
    team_data.inhibitor_kills = team["objectives"]["inhibitor"]["kills"]
    team_data.first_herald = team["objectives"]["riftHerald"]["first"]
    team_data.herald_kills = team["objectives"]["riftHerald"]["kills"]
    team_data.won = team["win"]

    team_scores[team_color] = team_data

print(team_scores["blue"].first_baron)

