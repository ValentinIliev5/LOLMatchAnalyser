import ujson
import utils
import csv

dataF = open('cleanedData.json')
full_data = ujson.load(dataF)

dataF.close()
file_name = "matches_data.csv"
with open(file_name, 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(utils.get_fields())


# teamId: 100 = blue 200 = red
    error_count = 0
    for i in range(0, len(full_data)):
        try:
            game_data = full_data[i]
            info = game_data["info"]
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

                player_data = utils.get_player_data(participant)

                player_dict = {participant["teamPosition"]: player_data}

                player_scores[team_color][participant["teamPosition"]] = player_data

            team_scores = {"blue": {}, "red": {}}

            for team in teams:
                team_color = "blue" if team["teamId"] == 100 else "red"

                team_data = utils.get_team_data(team)

                team_scores[team_color] = team_data

            line = utils.join_line_for_csv(player_scores, team_scores, red_pings, blue_pings)

            writer.writerow(line)
        except KeyError:

            print("error on line", i)
            error_count += 1

    print("errors: ", error_count)
