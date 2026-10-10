import truthTables

def correctInput(choice):
    if choice == "1" or choice == "2":
        while True:
            value = input("Input 1 or 0: ")
            if value.isnumeric():
                value = int(value)
                if (value == 0 or value == 1):
                    break
            print("Invalid input, try again")
        return value
    else:
        while True:
            value1 = input("Input 1 or 0 for first value: ")
            value2 = input("Input 1 or 0 for second value: ")
            if value1.isnumeric() and value2.isnumeric():
                value1 = int(value1)
                value2 = int(value2)
                if (value1 == 0 or value1 == 1) and (value2 == 0 or value2 == 1):
                    break
            print("Invalid input, try again")
        return value1, value2

def userInputs(choice, mode):
    if choice == "1" or choice == "2":
        print(f"Mode selected: {mode}")
        if choice == "1":
            value = correctInput(choice)
            newValue = truthTables.yesFunction(value)
            print(f"In {mode} mode, the value {value} became {newValue}")
        else:
            value = correctInput(choice)
            newValue = truthTables.notFunction(value)
            print(f"In {mode} mode, the value {value} became {newValue}")
    else:
        print(f"Mode selected: {mode}")
        if choice == "3":
            values = correctInput(choice)
            value1 = values[0]
            value2 = values[1]
            newValue = truthTables.andFunction(value1, value2)
            print(f"In {mode} mode, the values {value1} and {value2} resulted in {newValue}")
        elif choice == "4":
            values = correctInput(choice)
            value1 = values[0]
            value2 = values[1]
            newValue = truthTables.orFunction(value1, value2)
            print(f"In {mode} mode, the values {value1} and {value2} resulted in {newValue}")
        elif choice == "5":
            values = correctInput(choice)
            value1 = values[0]
            value2 = values[1]
            newValue = truthTables.nandFunction(value1, value2)
            print(f"In {mode} mode, the values {value1} and {value2} resulted in {newValue}")
        elif choice == "6":
            values = correctInput(choice)
            value1 = values[0]
            value2 = values[1]
            newValue = truthTables.norFunction(value1, value2)
            print(f"In {mode} mode, the values {value1} and {value2} resulted in {newValue}")
        elif choice == "7":
            values = correctInput(choice)
            value1 = values[0]
            value2 = values[1]
            newValue = truthTables.xorFunction(value1, value2)
            print(f"In {mode} mode, the values {value1} and {value2} resulted in {newValue}")
        else:
            values = correctInput(choice)
            value1 = values[0]
            value2 = values[1]
            newValue = truthTables.xnorFunction(value1, value2)
            print(f"In {mode} mode, the values {value1} and {value2} resulted in {newValue}")

options = {
    "1": "yes",
    "2": "not",
    "3": "and",
    "4": "or",
    "5": "nand",
    "6": "nor",
    "7": "xor",
    "8": "xnor",
}

while True:
    userchoice = input("which truth table would you want to check?\n[1] yes\n[2] not\n[3] and\n[4] or\n[5] nand\n[6] nor\n[7] xor\n[8] xnor\n[q] quit\nyour choice: ")
    if userchoice.isnumeric() and 1 <= int(userchoice) <= 8:
        num = userchoice
        mode = options[userchoice]
        userInputs(num, mode)
    elif userchoice == "q":
        break
    else:
        print("wrong input, try again")
