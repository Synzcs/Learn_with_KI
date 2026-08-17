from Mainchar import Player
from Enemy import Slime
import ByteLogic

p = Player.Player()
p.askname()
p.showstats()
while True:
    p.checkalive()
    choice = p.nextmove()
    if choice:
        break
    ByteLogic.chechfight()