import ujson
import utils

dataF = open('cleanedData.json')
full_data = ujson.load(dataF)

dataF.close()

# teamId: 100 = blue 200 = red

random_game = full_data[3]
info = random_game["info"]
participants = info["participants"]

game_duration = info["gameDuration"]
queue_id = info["queueId"]

player_scores = {"blue": {}, "red": {}}

blue_pings, red_pings = 0, 0

for participant in participants:
    b, r = utils.get_pings(participant)
    blue_pings += b
    red_pings += r

    team_color = "blue" if participant["teamId"] == 100 else "red"

    kills = participant["kills"]
    deaths = participant["deaths"]
    assists = participant["assists"]

    player_dict = {participant["teamPosition"]: (kills, deaths, assists)}

    player_scores[team_color][participant["teamPosition"]] = (kills, deaths, assists)
    #print("team:", team_color, participant["teamPosition"], participant["championName"], kills, deaths, assists)

print(player_scores)
