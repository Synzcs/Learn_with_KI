
def user_input():
    decision = str(input("l = countletters, w = countwords, o = longestword,s = write a story,d = delete, q = quit "))
    return decision

def writestory():
    story = str(input("Write a Story: "))
    stfile = open("Story.txt", "w", encoding="utf-8")
    stfile.write(story)
    stfile.close()


def countletters():
    stfile = open("Story.txt", "r", encoding="utf-8")
    story = stfile.read()
    letters = len(story)
    stfile.close()
    return letters

def countwords():
    stfile = open("Story.txt", "r", encoding="utf-8")
    story = stfile.read()
    words = story.split()

    stfile.close()
    return len(words)

def longestword():
    stfile = open("Story.txt", "r", encoding="utf-8")
    story = stfile.read()
    words = story.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    stfile.close()
    return longest

def deletetrace():
    stfile = open("Story.txt", "w", encoding="utf-8")
    stfile.close()

def runthrough():
    choice = user_input()
    if choice == "s":
        writestory()
    elif choice == "l":
        letters = countletters()
        countletters()
        print(letters)
    elif choice == "w":
        countwords()
        words = countwords()
        print(words)
    elif choice == "o":
        longestword()
        longest = longestword()
        print(longest)
    elif choice == "d":
        deletetrace()
    elif choice == "q":
        return True
    else:
        print("Please enter a valid option")
    return False


