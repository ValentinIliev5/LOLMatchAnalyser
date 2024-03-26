# import json
import ujson

dataF = open('matchesData.json')

data = ujson.load(dataF)

dictionary = data[0]
info = dictionary["info"]
participants = info["participants"]

game_duration = info["gameDuration"]
queue_id = info["queueId"]


for value in participants[0]:
    print(value)
