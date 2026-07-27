class Enemy:
    def __init__(self, levl=1):
        self.levl = levl
        self.HP = 80 + (levl * 20)      # Basis-HP skaliert mit Level
        self.damage = 5 + (levl * 5)    # Schaden skaliert mit Level

    # Berechnet die XP: Höheres Level bringt mehr XP
    def get_xp_reward(self):
        return self.levl * 5

    def stats(self):
        print(f"--- Gegner Status ---")
        print(f"HP: {self.HP} | Level: {self.levl}")
        print(f"---------------------")
