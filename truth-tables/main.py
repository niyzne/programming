import truthTables

def userInputs(choice, mode):
    if choice == "1" or choice == "2":
        print(f"Mode selected: {mode}")
        if choice == "1":
            while True:
                value = int(input("Input 1 or 0: "))
                if value == 0 or value == 1:
                    break
                print("Invalid input, try again")
            newValue = truthTables.yesFunction(value)
            print(f"In {mode} mode, the value {value} became {newValue}")
        else:
            while True:
                value = int(input("Input 1 or 0: "))
                if value == 0 or value == 1:
                    break
                print("Invalid input, try again")
            newValue = truthTables.notFunction(value)
            print(f"In {mode} mode, the value {value} became {newValue}")
    else:
        print(f"Mode selected: {mode}")
        if choice == "3":
            while True:
                value1 = int(input("Input 1 or 0 for first value: "))
                value2 = int(input("Input 1 or 0 for second value: "))
                if (value1 == 0 or value1 == 1) and (value2 == 0 or value2 == 1):
                    break
                print("Invalid input, try again")
            newValue = truthTables.andFunction(value1, value2)
            print(f"In {mode} mode, the values {value1} and {value2} resulted in {newValue}")
        elif choice == "4":
            while True:
                value1 = int(input("Input 1 or 0 for first value: "))
                value2 = int(input("Input 1 or 0 for second value: "))
                if (value1 == 0 or value1 == 1) and (value2 == 0 or value2 == 1):
                    break
                print("Invalid input, try again")
            newValue = truthTables.orFunction(value1, value2)
            print(f"In {mode} mode, the values {value1} and {value2} resulted in {newValue}")
        elif choice == "5":
            while True:
                value1 = int(input("Input 1 or 0 for first value: "))
                value2 = int(input("Input 1 or 0 for second value: "))
                if (value1 == 0 or value1 == 1) and (value2 == 0 or value2 == 1):
                    break
                print("Invalid input, try again")
            newValue = truthTables.nandFunction(value1, value2)
            print(f"In {mode} mode, the values {value1} and {value2} resulted in {newValue}")
        elif choice == "6":
            while True:
                value1 = int(input("Input 1 or 0 for first value: "))
                value2 = int(input("Input 1 or 0 for second value: "))
                if (value1 == 0 or value1 == 1) and (value2 == 0 or value2 == 1):
                    break
                print("Invalid input, try again")
            newValue = truthTables.norFunction(value1, value2)
            print(f"In {mode} mode, the values {value1} and {value2} resulted in {newValue}")
        elif choice == "7":
            while True:
                value1 = int(input("Input 1 or 0 for first value: "))
                value2 = int(input("Input 1 or 0 for second value: "))
                if (value1 == 0 or value1 == 1) and (value2 == 0 or value2 == 1):
                    break
                print("Invalid input, try again")
            newValue = truthTables.xorFunction(value1, value2)
            print(f"In {mode} mode, the values {value1} and {value2} resulted in {newValue}")
        else:
            while True:
                value1 = int(input("Input 1 or 0 for first value: "))
                value2 = int(input("Input 1 or 0 for second value: "))
                if (value1 == 0 or value1 == 1) and (value2 == 0 or value2 == 1):
                    break
                print("Invalid input, try again")
            newValue = truthTables.xnorFunction(value1, value2)
            print(f"In {mode} mode, the values {value1} and {value2} resulted in {newValue}")

while True:
    userChoice = input("Which truth table would you want to check?\n[1] yes\n[2] not\n[3] and\n[4] or\n[5] nand\n[6] nor\n[7] xor\n[8] xnor\n[q] quit\nYour choice: ")
    if userChoice == "1":
        userInputs("1", "yes")
    elif userChoice == "2":
        userInputs("2", "not")
    elif userChoice == "3":
        userInputs("3", "and")
    elif userChoice == "4":
        userInputs("4", "or")
    elif userChoice == "5":
        userInputs("5", "nand")
    elif userChoice == "6":
        userInputs("6", "nor")
    elif userChoice == "7":
        userInputs("7", "xor")
    elif userChoice == "8":
        userInputs("8", "xnor")
    elif userChoice == "q":
        break
    else:
        print("wrong input, try again")
