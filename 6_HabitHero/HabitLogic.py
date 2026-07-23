import datetime

cont = ""

def track_habit():
    amount = int(input("How much do you want to track?"))
    i = 0

    l = amount
    date = str(datetime.date.today())
    t = open("habits.txt", "a", encoding="utf-8")
    t.write("\n" + date + "\n")
    while i < amount:
        h = ""
        h = str(input("What habit did you complete? "))
        t.write(h + "\n")
        i += 1
    s = 0
    while s < 50:
        t.write("_")
        s += 1
    t.close()

def view_habits():
    v = open("habits.txt", "r", encoding="utf-8")
    read = v.read()
    print(read)
    v.close()


def decision():
    cont = str(input("Do you want to continue?(y/n)"))
    if cont == "y":
        wich = str(input("t = track habits, v = view habits"))
        if wich == "t":
            track_habit()
        elif wich == "v":
            view_habits()
    else:
        return True
    return False




