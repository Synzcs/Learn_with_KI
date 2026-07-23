
def write():
    writefile = str(input("Write your file name here: "))
    wfile = open(writefile, "w")
    written = str(input("Write what6 you want in your file"))
    wfile.write(written)
    wfile.close()

def reading():
    readfile = str(input("Write your file name here: "))
    rfile = open(readfile, "r")
    read = rfile.read()
    print(read)
    rfile.close()

def append():
    appendfile = str(input("Write your file name here: "))
    afile = open(appendfile, "a")
    afile.write("\n" + str(input("Write what6 you want in your file")))
    afile.close()

def checkwritten():
    auswahl = str(input("Write a for append, w for write, r for read and q to exit."))
    if auswahl == "w":
        write()
    elif auswahl == "r":
        reading()
    elif auswahl == "a":
        append()

    elif auswahl == "q":
        return True

    return False

