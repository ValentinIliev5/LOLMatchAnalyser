def get_pings(participant):
    blue_pings, red_pings = 0, 0
    for value in participant:
        if "pings" in value.lower():
            if participant["teamId"] == 100:
                blue_pings += participant[value]
            else:
                red_pings += participant[value]
    return blue_pings, red_pings