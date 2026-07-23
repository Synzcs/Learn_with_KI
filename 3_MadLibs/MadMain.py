import MadLogic

while True:
    quit_program = MadLogic.iputs()

    if quit_program:
        print("Goodbye!")
        break

    MadLogic.read_write()
    MadLogic.endoutputs()