from Mainchar import Player
from Enemy import Slime

p = Player.Player()
p.askname()
p.showstats()
while True:
    p.checkalive()
    choice = p.nextmove()
    if choice == "s":
        file = open("../Files/typeenemy.txt", "r")
        typeenemy = file.read()
        file.close()
        if typeenemy == 1:
            s = Slime.Slime()
            while True:
                pass

    elif choice:
        break
