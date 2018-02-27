
while True:

    print("Encryption editor:")
    print("...................")

    print("Do you want to encrypt or decrypt?")
    print("1) Encrypt")
    print("2) Decrypt")

    var = int(input())
    key = 10;
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



