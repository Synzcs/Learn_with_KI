from Mainchar import Player
from Enemy import Slime

def chechfight():
    file = open("../Files/fightstatus.txt", "r")
    status = file.read()
    file.close()
    if str(status) == "yes":
        file = open("../Files/typeenemy.txt", "r")
        typeenemy = file.read()
        file.close()
        if int(typeenemy) == 1:
            i = 5
            file = open("../Files/fightstatus.txt", "w")
            status = "no"
            file.write(status)
            file.close()
        elif int(typeenemy) == 2:
            file = open("../Files/fightstatus.txt", "w")
            status = "no"
            file.write(status)
            file.close()
        elif int(typeenemy) == 3:
            file = open("../Files/fightstatus.txt", "w")
            status = "no"
            file.write(status)
            file.close()

def makeslime():
    s = Slime.Slime()

def fight():
    pass




