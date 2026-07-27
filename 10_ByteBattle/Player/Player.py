from Enemy import Slime
from Enemy.Slime import Slime


class Mainchar:
    def __init__(self):
        self.fistattak = 2
        self.weaponmastery = 1
        self.kick = 3
        self.levl = 0
        self.XP = 0
        self.HP = 100

    def levelup(self):
        self.XP += 1
        print(self.XP)
        target_level = self.XP // 5
        if target_level > self.levl:
            self.leveleffects()
        return self.XP

    def leveleffects(self):
        self.levl += 1
        self.kick += 2
        self.weaponmastery += 1
        self.fistattak += 2
        self.HP += 2
        print("You accieved a level upgrade. New level: ", self.levl)
        self.points()

    def checkatk(self):
        typen = input("f = fist, k = kick\n")
        if typen == "f":
            self.fist()
        elif typen == "k":
            self.kik()



    def fist(self,slime):
        damage = self.fistattak
        slime.health -= damage


    def kik(self, slime):
        damage = self.kick
        slime.health -= damage

    def weaponmastery(self):
        mastery = self.weaponmastery
        return mastery

    def points(self):
        print("HP: ", self.HP)
        print("Kick: ", self.kick)
        print("Fist: ", self.fistattak)
        print("Weaponmastery: ", self.weaponmastery)


