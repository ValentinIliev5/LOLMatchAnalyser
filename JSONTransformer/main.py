import ujson

dataF = open('cleanedData.json')
full_data = ujson.load(dataF)

dataF.close()

random_game = full_data[7]
info = random_game["info"]
participants = info["participants"]

game_duration = info["gameDuration"]
queue_id = info["queueId"]

print(participants[5]["lane"])
for value in participants[0]:
    print(value)
