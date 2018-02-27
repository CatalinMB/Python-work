import time

# Open a file
try:

    # line = fHandle.readline()

    # for line in fHandle.readlines():
    #     print(line.rstrip("\n"))

    # allLines = fHandle.readlines()
    # print(len(allLines))

    # allLinesAsAString = fHandle.read()
    # print(type(allLinesAsAString))
    # print(fHandle.readline())
    # print(next(fHandle))
    # fHandle = open("test.txt","w")

    with open("test.txt","a") as handle:
        while True:
            newLine = input(":")
            if newLine != "\q":
                handle.write(newLine+"\n")
            if newLine == "\q":
                break

    # linenr = 1
    #
    # for line in fHandle.readlines():
    #     print("[" + str(linenr) +"]", line.rstrip())




    # startTime = time.time()
    #
    # for i in range (100):
    #     fHandle.write(str(i) + "\n")
    #
    # print("Time elapsed: ", time.time() - startTime)

    # while True:
    #
    #
    #     print("Awsome file Reader")
    #     print("......................")
    #     print("1) Read 1 line")
    #     print("2) Read all lines")
    #     print("3) Search for word")
    #     print("4) quit")
    #
    #     i = input("Please choose an option: ");
    #
    #     if i== "1":
    #         fHandle = open("test.txt")
    #         print(fHandle.readline())
    #         fHandle.close()
    #     elif i== "2":
    #         print(fHandle.readlines())
    #     elif i== "3":
    #
    #         # Linear search
    #         word = input("Please input a word to search for:")
    #         fHandle = open("test.txt")
    #         for line in fHandle.readline():
    #             if word in line:
    #                 print("We found your word: ", "["+line+"]")
    #         fHandle.close()
    #
    #     elif i== "4":
    #         print("Quitting...")
    #         break
    #     else:
    #         print("Invalid choice")






except FileNotFoundError:
    print("File does not exist")
