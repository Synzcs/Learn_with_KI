class Mainchar():
    def __init__(self):
        self.fistattak = 2
        self.weaponmastery = 1
        self.kick = 3
        self.levl = 0
        self.XP = 0

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
        print("You accieved a level upgrade. New level: ", self.levl)
        print("Kick: ", self.kick)
        print("Fist: ", self.fistattak)
        print("Weaponmastery: ", self.weaponmastery)