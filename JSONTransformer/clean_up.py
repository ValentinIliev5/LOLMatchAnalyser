import ujson

data_first_F = open('matchesDataFirst.json')

data_second_F = open('matchesData.json')

data_first = ujson.load(data_first_F)
data_second = ujson.load(data_second_F)

data_first_F.close()
data_second_F.close()

good_queues = [400, 420, 440]

filtered_data = [element for element in data_first + data_second
                 if element is not None
                 and element["info"]["queueId"] in good_queues]

faults = 0

for element in filtered_data:
    try:
        print(element["info"]["queueId"])
    except TypeError:
        faults = faults + 1

print("faults: ", faults)

print("old data size, new data size: ", len(data_first) + len(data_second),
      len(filtered_data))


print("test", len(filtered_data))

with open("cleanedData.json", "w") as outfile:
    ujson.dump(filtered_data, outfile)
