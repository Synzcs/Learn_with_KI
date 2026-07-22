

def rfile():
    score = 0
    username = input("Enter your username: ")
    if username == "q":
        return True
    readfile = open("Vocab.txt", "r", encoding="utf-8")
    for line in readfile:
        clean_line = line.strip()
        en_to_de = clean_line.split(",")
        en = en_to_de[0].strip()
        de = en_to_de[1].strip()
        print(en)
        german = str(input("Please enter the German word:"))
        if german == de:
            score = score + 1
            print("It was right your new score is: ", score," Points")
        else:
            print("It was wrong your score is still: ", score," Points")
    scoreboard = open("Scoreboard.txt", "a")
    scoreboard.write(username + ": " + str(score) + " Points\n")
    scoreboard.close()
    scoreboard = open("Scoreboard.txt", "r", encoding="utf-8")
    read = scoreboard.read()
    print(read)
    readfile.close()
    scoreboard.close()
    return False




