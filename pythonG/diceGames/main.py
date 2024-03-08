def main():
    import dice
    import moneyhand as mh
    import json


    money = 0
    dice.clear()
    q = dice.Dice()
    q.settings(10, 1)
    q.set(4)
    rol = q.roll()
    money = money + rol
    mh.save(q)

if __name__ == "__main__":
    main()