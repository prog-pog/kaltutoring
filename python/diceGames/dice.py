from time import sleep as wait
import random
from os import system, name


def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class Dice:
    def settings(self, delay):
        self.delay = delay
    def set(self, sides, mult):
        self.multi = mult
        self.sides = sides
        self.name = "d"+sides
    def roll(self):
        for i in range(self.delay):
            print(self.name)
            print("")
            print(random.randint(1,self.sides))
            wait(0.2)
        print(self.name)
        print("")
        print((random.randint(1,self.sides)*self.multi))

def create(sides, mult, delay, nam):
    nam = Dice()
    nam.settings(delay)
    nam.set(sides, mult)
    return nam