import json
import time
import requests

# https://127.0.0.1:2999/swagger/v3/openapi.json

LOCALHOST = "https://127.0.0.1:2999/liveclientdata/allgamedata"
LIVE_GAME_STATS = "https://127.0.0.1:2999//liveclientdata/gamestats"
LOCAL_LIVE_URL = "liveclientdata/allgamedata"


def getAllGameData():
    return requests.get(f"{LOCALHOST}", verify=False).json()

def gameStats():
    return requests.get(f"{LIVE_GAME_STATS}", verify=False).json()

def write_to_file(data, filename):
    with open(f"{filename}.json", "w") as outfile:
        outfile.write(data)

def loop():
    while(True):
        temp = getAllGameData()
        print(temp)
        write_to_file(json.dumps(temp, indent=4), "all_stats")
        write_to_file(json.dumps(gameStats(), indent=4), "game_stats")
        time.sleep(5)

loop()