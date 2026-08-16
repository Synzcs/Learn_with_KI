import random

from Game import ByteLogic

class Slime:
        def __init__(self):
            self.name = "Slime"
            self.level = 1
            self.HP = 10
            self.Kicks = 2
            self.Punch = 2

        def getPLevel(self):
            file = open("../Files/level.txt", "r")
            Plevel = file.read()
            file.close()
            return Plevel

        def setLevel(self):
            PLevel = self.getPLevel()
            addition =random.randint(1, 3)
            self.level = int(PLevel) + addition

        def setstats(self):
            slevel = self.level()
            if self.level > 1:
                i = slevel - 1
                while i > 0:
                    self.HP += 5
                    self.Kicks += 5
                    self.Punch += 5
                    i -= 1

        def showmyself(self):
            print("Neuer Gegner!")
            print("Name: ", self.name)
            print("Level: ", self.level)

