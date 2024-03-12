import base64
import json


try:
    readFrom = open("python/randEnc/text.txt", "r")
    s1 = readFrom.readlines()
    print(s1)
    save = json.loads(s1[0].encode())
    text = s1[1].encode()
    for i in range(len(save)):
        if save[i] == "1":
            text = base64.b85decode(text)
        else:
            text = base64.b64decode(text)
    text = json.dumps(text.decode())
    print(text)
except:
    raise