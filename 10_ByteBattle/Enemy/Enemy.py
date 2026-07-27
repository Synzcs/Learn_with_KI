class Enemy:
    def __init__(self):
        self.health = 0
        self.level = 0
        self.mastery = 0

    def stats(self):
        print("HP: ", self.health)
        print("Level: ", self.level)
