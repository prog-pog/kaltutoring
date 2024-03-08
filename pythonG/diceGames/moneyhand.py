import json


def save(dice):
    data = json.dumps(dice.__dict__, indent=4)
    with open("save.json", "w") as file:
        file.flush()
        file.write(data)
    file.close()

def load():
    try:
        with open("save.json", "r") as file:
            data = file.read()
        file.close()
        print(data)
    except FileNotFoundError:
        exit()