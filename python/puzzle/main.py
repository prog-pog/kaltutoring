import random


score = 0
table1 = [["·", "·", "·"],
    ["·", "·", "·"],
    ["·", "·", "·"]
]
table2 = [["·", "·", "·"],
    ["·", "·", "·"],
    ["·", "·", "·"]
]
table3 = [["·", "·", "·"],
    ["·", "·", "·"],
    ["·", "·", "·"]
]
while True:
    print("1:")
    for i in table1:
        for j in i:
            print(j, end=" ")
        print()
    print("2:")
    for i in table2:
        for j in i:
            print(j, end=" ")
        print()
    print("3:")
    for i in table3:
        for j in i:
            print(j, end=" ")
        print()
    new = [["·", "·", "·"],
        ["·", "·", "·"],
        ["·", "·", "·"]
    ]
    co = random.randint(0, 2)
    co2 = random.randint(0, 2)
    new[co][co2] = "◦"
    print("new:")
    for i in new:
        for j in i:
            print(j, end=" ")
        print()
    print("score:", score)
    coi = int(input("1, 2 or 3?\n"))
    if coi >= 4 or coi <= 0:
        exit("incorrect input")
    elif coi == 1:
        table1[co][co2] = "◦"
    elif coi == 2:
        table2[co][co2] = "◦"
    elif coi == 3:
        table3[co][co2] = "◦"
    else:
        exit("good job, you broke it :\\")
    if table1 == [["◦", "◦", "◦"], ["◦", "◦", "◦"], ["◦", "◦", "◦"]]:
        table1 = [["·", "·", "·"], ["·", "·", "·"], ["·", "·", "·"]]
        table2 = [["·", "·", "·"], ["·", "·", "·"], ["·", "·", "·"]]
        score = score + 150
    if table2 == [["◦", "◦", "◦"], ["◦", "◦", "◦"], ["◦", "◦", "◦"]]:
        table1 = [["·", "·", "·"], ["·", "·", "·"], ["·", "·", "·"]]
        table2 = [["·", "·", "·"], ["·", "·", "·"], ["·", "·", "·"]]
        table3 = [["·", "·", "·"], ["·", "·", "·"], ["·", "·", "·"]]
        score = score + 200
    if table3 == [["◦", "◦", "◦"], ["◦", "◦", "◦"], ["◦", "◦", "◦"]]:
        table3 = [["·", "·", "·"], ["·", "·", "·"], ["·", "·", "·"]]
        table2 = [["·", "·", "·"], ["·", "·", "·"], ["·", "·", "·"]]
        score = score + 150