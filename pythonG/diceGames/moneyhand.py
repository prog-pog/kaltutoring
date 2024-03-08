import json
import base64


def save(dice):
    data = json.dumps(dice, indent=4)
    with open("pythonG/diceGames/save.json", "w") as file:
        file.flush()
        file.write(data)
    file.close()

def load():
    try:
        with open("pythonG/diceGames/save.json", "r") as file:
            data = json.loads(file.read())
        file.close()
    except FileNotFoundError:
        with open("pythonG/diceGames/save.json", "w") as file:
            file.flush()
            data = {"delay": 20, "mult": 1, "sides": 2, "money": 0}
            data = json.dumps(data, indent=4)
            file.write(data)
        file.close()
        assert True
    except:
        raise
    return data