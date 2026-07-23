story = ""
adj = ""
nam = ""
noun = ""
crea = ""
num = ""

def read_write():
    global story
    ofile = open("story.txt","r+",encoding="utf-8")
    story = ofile.read()



def iputs():
    global adj, nam, noun, crea, num
    quit = str(input("wanna quit? y/n: "))
    if quit == "y":
        return True

    adj = str(input("Enter an random adjective: "))
    nam = str(input("Enter an random name: "))
    noun = str(input("Enter an random noun: "))
    crea = str(input("Enter an random Name for a animal/craeature: "))
    num = str(input("Enter an random number: "))
    return False


def endoutputs():
    #global story, adj, nam, noun, crea, num
    global story

    story = story.replace("[ADJECTIVE]", adj )
    story = story.replace("[NAME]", nam )
    story = story.replace("[NOUN]", noun )
    story = story.replace("[CREATURE]", crea )
    story = story.replace("[NUMBER]", num )
    print(story)


