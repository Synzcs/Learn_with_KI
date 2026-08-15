from Mainchar import Player

p = Player.Player()
p.askname()
p.showstats()
while True:
    p.checkalive()
    choice = p.nextmove()
    if choice:
        break
