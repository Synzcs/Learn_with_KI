import random
from Enemy.Enemy import Enemy

class Slime(Enemy):
    def __init__(self):
        super().__init__()
        self.level = random.randint(1, 6)
        self.jumpatk = 0
        self.damage = 0

    def checklevl(self):
        if self.level == 1:
            self.health = 10
            self.jumpatk = 2
        elif self.level == 2:
            self.health = 15
            self.jumpatk = 4
        elif self.level == 3:
            self.health = 20
            self.jumpatk = 6
        elif self.level == 4:
            self.health = 25
            self.jumpatk = 8
        elif self.level == 5:
            self.health = 30
            self.jumpatk = 10

    def jumpa(self, player):
        damage = self.jumpatk
        player.HP -= damage






