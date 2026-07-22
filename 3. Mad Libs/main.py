import Logic

while True:
    quit_program = Logic.iputs()

    if quit_program:
        print("Goodbye!")
        break

    Logic.read_write()
    Logic.endoutputs()