
def add_task():
    a = open("tasks.txt", "a", encoding="utf-8")
    task = input("Enter your task: ")
    imp = str(input("Enter your importance(1 = High, 2 = Medium, 3 = Low): "))
    a.write(imp +","+ task + "\n")
    a.close()

def view_tasks():
    all_tasks = []
    v = open("tasks.txt", "r", encoding="utf-8")
    for line in v:
        clean_line = line.strip()
        priority, task = clean_line.split(",")
        all_tasks.append([priority,task])
    v.close()
    all_tasks.sort()
    print("\n--- YOUR SORTED TASKS ---")
    for item in all_tasks:

        print(f"Priority {item[0]}: {item[1]}")
    print("-------------------------\n")




def delete_tasks():
    d = open("tasks.txt", "w", encoding="utf-8")
    d.close()
    print("Tasks deleted")

def runtrhough():
    decision = input("Enter your decision( a = add task, v = view tasks, d = delete all tasks, q = quit): ")
    if decision == "a":
        add_task()
    elif decision == "v":
        view_tasks()
    elif decision == "d":
        delete_tasks()
    elif decision == "q":
        return True
    return False


