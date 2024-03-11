import json
import base64


def save(dice):
    data = json.dumps(dice)
    data = data.encode()
    data = base64.b64encode(data)
    with open("python/diceGames/save.txt", "w") as file:
        file.flush()
        data = data.decode()
        file.write(data)
    file.close()

def load():
    try:
        with open("python/diceGames/save.txt", "r") as file:
            data = base64.b64decode(file.read())
            print(data)
            data = data.decode()
            print(data)
            data = json.loads(data)
            print(type(data))
        file.close()
    except FileNotFoundError:
        with open("python/diceGames/save.txt", "w") as file:
            file.flush()
            data = {"delay": 20, "mult": 1, "sides": 2, "money": 0}
            data = json.dumps(data)
            data = data.encode()
            data = base64.b64encode(data)
            file.write(data)
        file.close()
    except:
        raise
    return data