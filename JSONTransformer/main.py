# import json
import ujson

dataF = open('matchesData.json')

data = ujson.load(dataF)
dataF.close()


good_queues = [400, 420, 450]

filtered_data = [element for element in data
                 if element is not None
                 and element["info"]["queueId"] in good_queues]

faults = 0

for element in filtered_data:
    try:
        print(element["info"]["queueId"])
    except TypeError:
        faults = faults + 1

print("faults: ", faults)

print("old data size, new data size: ", len(data), len(filtered_data))


# dictionary = data[7]
# info = dictionary["info"]
# participants = info["participants"]

# game_duration = info["gameDuration"]
# queue_id = info["queueId"]

# print(participants[5]["lane"])
# for value in participants[0]:
#    print(value)
