import random

gnum = 0

def generatenumber():
    global gnum
    gnum = random.randint(0,1000000)


def checkplace():
    all_scores = []
    highscore = open("Highscores.txt", "r", encoding="utf-8")
    read = highscore.readlines()
    for line in read:
        score_text, user = line.strip().split(",")
        score_num = int(score_text)
        all_scores.append([score_num, user])
    all_scores.sort()
    print(all_scores[:10])
    highscore.close()

def runthru():
    start = str(input("Do you wanna start(y = yes,q = quit,c = check Highscores)?: "))
    if start == "y":
        user = str(input("Enter your username: "))
        generatenumber()
        score = 0
        while True:
            hey = gnum
            print(hey)  # Zum Testen
            guess = int(input("Guess the number (0 - 1 million): "))
            score += 1
            if guess == gnum:
                print(f"Correct! You needed {score} attempts.")
                break
            elif guess < gnum:
                print("too low")
            elif guess > gnum:
                print("too high")
        turnin = open("Highscores.txt", "a", encoding="utf-8")
        turnin.write(str(score) + "," + user + "\n")
        turnin.close()
    elif start == "q":
        return True
    elif start == "c":
        checkplace()
    return False

runthru()





