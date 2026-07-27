class Mainchar:
    def __init__(self):
        self.fistattak = 2
        self.weapon_mastery_val = 1
        self.kick = 3
        self.levl = 0
        self.XP = 0
        self.HP = 100
        self.max_HP = 100  # Speichert das maximale Leben für die Heilung

    def add_xp(self, amount):
        self.XP += amount
        print(f"✨ Du erhältst {amount} XP! (Gesamt-XP: {self.XP})")

        # Prüfen, ob genug XP für ein oder mehrere Level-Ups da sind
        while self.XP >= (self.levl + 1) * 5:
            self.leveleffects()

    def leveleffects(self):
        self.levl += 1
        self.kick += 2
        self.weapon_mastery_val += 1
        self.fistattak += 2
        self.max_HP += 10  # Max-HP erhöht sich
        self.HP = self.max_HP  # Volle Heilung bei Level-Up
        print(f"\n🎉 LEVEL UP! Du bist jetzt Level {self.levl}!")
        self.points()

    def rest(self):
        self.HP = self.max_HP
        print(f"💤 Du hast geschlafen und dich komplett erholt! Deine HP sind wieder bei {self.HP}.\n")

    def checkatk(self, enemy):
        typen = input("f = fist, k = kick\n")
        if typen == "f":
            self.fist(enemy)
        elif typen == "k":
            self.kik(enemy)

    def fist(self, enemy):
        damage = self.fistattak
        enemy.HP -= damage
        print(f"Du schlägst zu! Der Gegner verliert {damage} HP.")

    def kik(self, enemy):
        damage = self.kick
        enemy.HP -= damage
        print(f"Du trittst zu! Der Gegner verliert {damage} HP.")

    def points(self):
        print(f"HP: {self.HP}/{self.max_HP} | Kick: {self.kick} | Fist: {self.fistattak}")
