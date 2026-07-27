from Enemy.Enemy import Enemy

class Slime(Enemy):
    def __init__(self, levl=1):
        super().__init__(levl)
        # Slime-Spezifische Werte (skalieren leicht mit dem Level)
        self.HP = 15 + (levl * 5)
        self.damage = 3 + (levl * 2)

    def checklevl(self):
        print(f"🐛 Ein wilder Slime erscheint! (Level {self.levl})")

    def jumpa(self, player):
        print("Der Slime springt und greift an!")
        player.HP -= self.damage
        print(f"Du verlierst {self.damage} HP! Deine verbleibenden HP: {player.HP}\n")
