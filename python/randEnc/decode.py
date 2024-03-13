import base64
import json


try:
    readFrom = open("python/randEnc/file.txt", "r")
    s1 = readFrom.readlines()
    s11 = s1[0].replace("\n", "")
    txt = base64.b32decode(s11)
    save = json.loads(txt.decode())
    text = s1[1].encode()
    for i in range(len(save)):
        if save[i] == "1":
            text = base64.b85decode(text)
        else:
            text = base64.b64decode(text)
    print(text.decode())
except:
    raise