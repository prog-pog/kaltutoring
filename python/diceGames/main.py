import moneyhand as mh


def main():
    import dice
    import moneyhand as mh


    data = mh.load()
    try:
        money = data["money"]
    except:
        exit("Please run main.py again.")
    dice.clear()
    q = dice.Dice()
    q.settings(data["delay"], data["mult"])
    q.set(data["sides"])
    rol = q.roll()
    money = money + rol
    print("{}$".format(money))
    save = {"delay" : data["delay"], "mult": data["mult"], "sides": data["sides"], "money": money}
    mh.save(save)

if __name__ == "__main__":
    while True:
        try:
            main()
            c = input("Options, [ENTER] = Continue, [M] = Shop, [E] = Exit\n")
            if c.capitalize() == "M":
                data = mh.load()
                o = input("1. Side = {0}$\n2. Mult = {1}$\n".format(int(data["sides"])*3**2, int(data["mult"])*10**3))
                if o == "1" and data["money"] >= int(data["sides"])*3**2:
                    money = data["money"] - int(data["sides"])*3**2
                    sides = int(data["sides"]) + 1
                    save = {"delay" : data["delay"], "mult": data["mult"], "sides": sides, "money": money}
                    mh.save(save)
                if o == "2" and data["money"] >= int(data["mult"])*10**3:
                    money = data["money"] - int(data["mult"])*10**3
                    mult = int(data["mult"]) + 1
                    save = {"delay" : data["delay"], "mult": mult, "sides": data["sides"], "money": money}
                    mh.save(save)
                else:
                    pass
            if c.capitalize() == "E":
                exit("")
            else: pass
        except KeyboardInterrupt:
            exit("\nOk, you ended it")