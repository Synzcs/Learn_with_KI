import random
import string

all_chars = string.ascii_letters + string.digits + string.punctuation

def generate_save():
    global all_chars
    site = str(input("What account is your password for: "))
    username = str(input("What is the username: "))
    passwordl = int(input("How long is the password: "))
    password = "".join(random.choices( all_chars, k=passwordl))
    d = open("Logindata.txt", "a", encoding="utf-8")
    d.write("\n" + site + "\n")
    d.write(username + "\n")
    d.write(password + "\n")
    i=0
    while i < 100:
        d.write("_")
        i+=1
    d.close()


def view_passwords():
    v = open("Logindata.txt", "r", encoding="utf-8")
    site = v.read()
    print(site)

def choose():
    choice = str(input("Choose your option(v = view, g = generate, q = quit: "))
    if choice == "v":
        view_passwords()
    elif choice == "g":
        generate_save()
    elif choice == "q":
        return True
    return False