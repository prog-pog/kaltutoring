import base64
import random
import json


ch = []
saveto = open("python/randEnc/text.txt", "w")
saveto.flush()
amm = random.randint(2, 4)
text = input("What do you want to convert?")
text = text.encode()
for i in range(amm):
    cho = random.randint(0, 1)
    ch.append(cho)
for i in range(amm):
    if ch[i] == "1":
        text = base64.b85encode(text)
    else:
        text = base64.b64encode(text)
save = json.dumps(ch)
saveto.write(save)
saveto.write(text.decode())