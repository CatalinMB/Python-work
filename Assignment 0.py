while True:

    print("---Note editor---")
    print("...................")

    print("What do you want to do?")
    print("1) Create a note")
    print("2) View all notes")
    print("3) Delete a note")

    print("...................")


    var = int(input())

    if var == 1:
        text = input("What word do you want to encrypt?:")

        for i in text:
            print(chr(ord(i)+key), end="")

        print("\n")
    elif var == 2:
        text = input("What word do you want to decrypt?:")

        for i in text:
            print(chr(ord(i)-key), end="")
        print("\n")
    else:
        break