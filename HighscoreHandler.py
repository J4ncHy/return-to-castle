import json
import requests

def write_score(level, score, time):
    scoreTemplate = {
        "player": "Player",
        "level": level+1,
        "score": score,
        "time": time
    }

    api_url = "https://rtc.picka.si/api/create"
    response = requests.put(api_url, json=scoreTemplate)

    print(response)

"""
    192.168.128.8:3012/api/create
    
    {
        "player": "Janchy",
        "level": 2,
        "score": 1232,
        "time": 25
    }
"""