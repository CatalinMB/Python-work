import datetime

while True:
    print("-- Log generator for variable --")
    # make a variable that needs to be changed and open the file
    # make variables that keeps the last change
    handler = open("log", "r")
    lines = handler.readlines()
    handler.close()
    handler = open("log", "a")
    line = lines[-1]
    x = line[(line.rfind(':')+1):line.rfind(';')]
    nr = line[28:(line.rfind('-')-1)]

    # takes user input and compare
    userNr = input("Change the variable x to : ")

    if userNr != x:
        x = userNr
        handler.write("\n" + str(datetime.datetime.now()) + " - " + str(int(nr)+1) + " - " + "Variable changed to: " + userNr + ";")
        handler.close()
        break
    else:
        print("Variable is not an int or is the same value!")


# write in the file : time - nr of change - Variable has changed to : input;



