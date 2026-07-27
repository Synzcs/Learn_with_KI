from Enemy.Slime import Slime
from Player.Player import Mainchar

Slime1 = Slime()
P1 = Mainchar()

Slime1.checklevl()

P1.levelup()
P1.leveleffects()
P1.fist()

Slime1.jumpa(P1)
Slime1.stats()

P1.points()
