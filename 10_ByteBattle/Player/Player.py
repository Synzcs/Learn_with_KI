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
        print("HP: ", self.HP)
        print("Kick: ", self.kick)
        print("Fist: ", self.fistattak)
        print("Weaponmastery: ", self.weaponmastery)

    def fist(self):
        damage = self.fistattak
        return damage

    def kik(self):
        damage = self.kick
        return damage

    def weaponmastery(self):
        mastery = self.weaponmastery


