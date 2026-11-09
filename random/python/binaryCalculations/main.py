import calculations as c

while True:
    userInput = input("What do you want to do?\n[1] Convert Intiger to Binary\n[2] Convert Binary to Intiger\n[q] Quit\nYour Choice: ")
    if userInput == "1":
        intNum = input("Enter a Number: ")
        if intNum.isnumeric():
            intNum = int(intNum)
            print(c.intToBin(intNum))
        else:
            print("Wrong input, Try again")
    elif userInput == "2":
        binNum = input("Enter a Binary Number: ")
        print(c.binToInt(binNum))
    elif userInput == "q":
        break
    else:
        print("Wrong input, Try again")
