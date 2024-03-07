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
    def settings(self, delay, mult):
        self.delay = delay
        self.multi = mult

    def set(self, sides):
        self.sides = sides
        self.name = "d"+str(self.sides)

    def roll(self):
        for i in range(self.delay):
            clear()
            print(self.name)
            print("")
            print(random.randint(1,self.sides))
            wait(0.3)
        clear()
        print(self.name)
        print("")
        self.ro = random.randint(1,self.sides)
        self.rol = self.ro*self.multi
        print(self.ro,"*",self.multi,"=",self.rol+"$")