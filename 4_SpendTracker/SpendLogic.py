

total_spendings = 0.0
total_incomes = 0.0
def addexpense():
    reason = str(input("What did you buy: "))
    spending = int(input("How much money: "))
    s = open("Spendings.txt", "a", encoding="utf-8")
    s.write(str(spending) + ", " + reason  + "\n")
    s.close()

def addincome():
    reason = str(input("Why did you get your money: "))
    income = int(input("How much money: "))
    i = open("Incomes.txt", "a", encoding="utf-8")
    i.write(str(income) + ", " + reason + "\n")
    i.close()

def evaluate():
    global total_spendings, total_incomes
    total_incomes = 0
    total_spendings = 0
    es = open("Spendings.txt", "r", encoding="utf-8")
    ei = open("Incomes.txt", "r", encoding="utf-8")
    for line in es:
        worth = line.strip().split(",")
        total_spendings += float(worth[0])
    es.close()
    for line in ei:
        worth = line.strip().split(",")
        total_incomes += float(worth[0])
    ei.close()
    print("Income = ", total_incomes)
    print("Spendings = ", total_spendings)
    saldo = total_incomes - total_spendings
    print("Saldo = ",saldo)


def userinput():
    action = str(input("What do you want to do(s = Spending, i = Income, e = Evaluate, q = Quit): "))
    if action == "s":
        addexpense()
    elif action == "i":
        addincome()
    elif action == "e":
        evaluate()
    elif action == "q":
        return True

    return False

