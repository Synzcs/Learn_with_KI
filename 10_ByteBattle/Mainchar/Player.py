import random
import sys


class Player:
    def __init__(self):
        self.level = 0
        self.XP = 0
        self.name = ""
        self.health = 10
        self.health_max = 10
        self.weaponmastery = 0
        self.punch = 0
        self.kick = 0

    def askname(self):
        self.name = input("Please enter your name: ")

    def train(self):
        ask = str(input("What do you want to train?(k = Kicks, p = Punch, m = weaponmastery)"))
        trainefficient = random.randint(0,100)
        if trainefficient > 50:
            if ask == "k" and trainefficient > 90:
                self.kick += 3
                print("Congrats you got better at Kicks by 3 Points.")
            elif ask == "k" and trainefficient > 75:
                self.kick += 2
                print("Congrats you got better at Kicks by 2 Points.")
            elif ask == "k" and trainefficient > 50:
                self.kick += 1
                print("Congrats you got better at Kicks by 1 Point.")
            elif ask == "p" and trainefficient > 90:
                self.punch += 3
                print("Congrats you got better at Punch by 3 Points.")
            elif ask == "p" and trainefficient > 75:
                self.punch += 2
                print("Congrats you got better at Punch by 2 Points.")
            elif ask == "p" and trainefficient > 50:
                self.punch += 1
                print("Congrats you got better at Punch by 1 Point.")
            elif ask == "m" and trainefficient > 90:
                self.weaponmastery += 3
                print("Congrats you got better at Weaponmastery by 3 Points.")
            elif ask == "m" and trainefficient > 75:
                self.weaponmastery += 2
                print("Congrats you got better at Weaponmastery by 2 Points.")
            elif ask == "m" and trainefficient > 50:
                self.weaponmastery += 1
                print("Congrats you got better at Weaponmastery by 1 Point.")
            else:
                print("You didn't get better.")
        else:
            print("You didn't get better.")

    def showstats(self):
        print("name:", self.name)
        print("Level:", self.level)
        print("XP:", self.XP)
        print("health:", self.health)
        print("weaponmastery:", self.weaponmastery)
        print("punch:", self.punch)
        print("kick:", self.kick)

    def chckLevel(self):
        origXP = self.XP % 10
        if origXP == 0:
            self.level += 1
            self.Levelincrease()


    def Levelincrease(self):
        self.health_max += 5
        self.weaponmastery += 3
        self.punch += 3
        self.kick += 3
        self.showstats()

    def Kicking(self):
        damage = self.kick
        file = open("../Files/damage.txt", "w")
        file.write(str(damage))
        file.close()
        print("Damage: ", damage)

    def Punching(self):
        damage = self.punch
        file = open("../Files/damage.txt", "w")
        file.write(str(damage))
        file.close()
        print("Damage: ", damage)

    def attakdec(self):
        type = str(input("Do you want to perform a k = Kick or p = Punch?"))
        if type == "k":
            self.Kicking()
        elif type == "p":
            self.Punching()
        else:
            print("Your just dumb")

    def gothit(self):
        file = open("../Files/damage.txt", "r")
        damage = file.read()
        file.close()
        self.health = self.health - int(damage)
        print("Health: ", self.health)
        self.checkalive()

    def checkalive(self):
        live = self.health
        if live <= 0:
            print("You are dead")
            sys.exit()

    def searchenemy(self):
        self.sendstats()
        if self.level <= 5:
            l = 1
            file = open("../Files/typeenemy.txt", "w")
            file.write(str(l))
            file.close()
        elif self.level <= 10:
            l = 2
            file = open("../Files/typeenemy.txt", "w")
            file.write(str(l))
            file.close()
        elif self.level > 10:
            l = 3
            file = open("../Files/typeenemy.txt", "w")
            file.write(str(l))
            file.close()

    def sendstats(self):
        Level = self.level
        file = open("../Files/level.txt", "w")
        file.write(str(Level))
        file.close()

    def nextmove(self):
        decision = str(input("What do you want to do?(q = quit, c = checkstats, a = attak, t = train, g = gethit,s = searchenemy)"))
        if decision == "c":
            self.showstats()
        elif decision == "a":
            self.attakdec()
        elif decision == "t":
            self.train()
        elif decision == "g":
            self.gothit()
        elif decision == "s":
            self.searchenemy()
            file = open("../Files/fightstatus.txt", "w")
            yea = "yes"
            file.write(str(yea))
            file.close()
        elif decision == "q":
            return True
        return False
