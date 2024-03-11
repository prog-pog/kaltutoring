import json
import base64


def save(dice):
    data = json.dumps(dice)
    data = data.encode()
    data = base64.b64encode(data)
    data = base64.b85encode(data)
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
            data = base64.b85decode(data)
            data = base64.b64decode(data)
            data = data.decode()
            data = json.loads(data)
        file.close()
    except FileNotFoundError:
        with open("python/diceGames/save.txt", "w") as file:
            file.flush()
            data = {"delay": 20, "mult": 1, "sides": 2, "money": 0}
            data = json.dumps(data)
            data = data.encode()
            data = base64.b64encode(data)
            data = base64.b85encode(data)
            data = base64.b64encode(data)
            data = data.decode()
            file.write(data)
        file.close()
        pass
    except json.decoder.JSONDecodeError:
        with open("python/diceGames/save.txt", "r") as file:
            if file.read() == "":
                fil = open("python/diceGames/save.txt", "w")
                data = {"delay": 20, "mult": 1, "sides": 2, "money": 0}
                data = json.dumps(data)
                data = data.encode()
                data = base64.b64encode(data)
                data = base64.b85encode(data)
                data = base64.b64encode(data)
                data = data.decode()
                fil.write(data)
                fil.close()
            file.close()
        exit("File empty, replaced with starting file, Please run main.py again.")
    except:
        exit("Unknown Error, Possible data corruption. If this persists please delete save.txt")
    return data