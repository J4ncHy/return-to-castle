import json


def read_score():
    with open("data/highscore.json", "r") as openfile:
        json_object = json.load(openfile)
    openfile.close()

    return json_object


def write_score(level, score, time):
    arr = read_score()
    scoreTemplate = {
        "level": level+1,
        "score": score,
        "time": time
    }
    arr.append(scoreTemplate)
    json_object = json.dumps(arr, indent=4)
    with open("data/highscore.json", "w") as outfile:
        outfile.write(json_object)
    outfile.close()
