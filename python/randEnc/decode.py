import base64
import json


try:
    readFrom = open("python/randEnc/file.txt", "r")
    s1 = readFrom.readlines()
    txt = base64.b32decode(str(s1[0]).encode())
    save = json.loads(txt.encode())
    text = s1[1].encode()
    for i in range(len(save)):
        if save[i] == "1":
            text = base64.b85decode(text)
        else:
            text = base64.b64decode(text)
    text = text.decode()
except:
    raise