def main():
    import dice
    import moneyhand as mh


    mh.start()
    dice.clear()
    q = dice.Dice()
    q.settings(10, 1)
    q.set(4)
    q.roll()

if __name__ == "__main__":
    main()