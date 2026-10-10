import truthTables
import modes

colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "reset": "\033[0m"
}

options1 = {
    "1": "print logic gates",
    "2": "add or multiply"
}

options2 = {
    "1": "yes",
    "2": "not",
    "3": "and",
    "4": "or",
    "5": "nand",
    "6": "nor",
    "7": "xor",
    "8": "xnor"
}

options3 = {
    "1": "addition",
    "2": "multiplication"
}

def correctInput(choice):
    if choice == "1" or choice == "2":
        while True:
            value = input("Input 1 or 0: ")
            if value.isnumeric():
                value = int(value)
                if (value == 0 or value == 1):
                    break
            print(f'{colors["red"]}Invalid input, try again{colors["reset"]}')
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
            print(f'{colors["red"]}Invalid input, try again{colors["reset"]}')
        return value1, value2


def addOrMultiplyFunction(user_choice, mode):
    if mode == "addition":
        firstInput = input(f"For {mode}, what's the first operator we will perform?\n[1] yes\n[2] not\n[3] and\n[4] or\n[5] nand\n[6] nor\n[7] xor\n[8] xnor\n[q] quit\nyour choice: ")
        if firstInput.isnumeric() and 1 <= int(firstInput) <= 8:
            num = firstInput
            mode1Mode = options2[firstInput]
            first = userInputs(num, mode1Mode)
        elif firstInput == "q":
            print(f'{colors["blue"]}Have a good day{colors["reset"]}')
            return
        else:
            print(f'{colors["red"]}wrong input, try again{colors["reset"]}')
            return

        secondInput = input(f"For {mode}, what's the second operator we will perform?\n[1] yes\n[2] not\n[3] and\n[4] or\n[5] nand\n[6] nor\n[7] xor\n[8] xnor\n[q] quit\nyour choice: ")
        if secondInput.isnumeric() and 1 <= int(secondInput) <= 8:
            num = secondInput
            mode2Mode = options2[secondInput]
            second = userInputs(num, mode2Mode)
        elif secondInput == "q":
            print(f'{colors["blue"]}Have a good day{colors["reset"]}')
            return
        else:
            print(f'{colors["red"]}wrong input, try again{colors["reset"]}')
            return

        result = modes.addition(first, second)
        print(f'{colors["green"]}In {mode} mode, the {options2[firstInput]} and {options2[secondInput]} have resulted in {result}{colors["reset"]}')


    else: 
        firstInput = input(f"For {mode}, what's the first operator we will perform?\n[1] yes\n[2] not\n[3] and\n[4] or\n[5] nand\n[6] nor\n[7] xor\n[8] xnor\n[q] quit\nyour choice: ")
        if firstInput.isnumeric() and 1 <= int(firstInput) <= 8:
            num = firstInput
            mode1Mode = options2[firstInput]
            first = userInputs(num, mode1Mode)
        elif firstInput == "q":
            print(f'{colors["blue"]}Have a good day{colors["reset"]}')
            return
        else:
            print(f'{colors["red"]}wrong input, try again{colors["reset"]}')
            return

        secondInput = input(f"For {mode}, what's the second operator we will perform?\n[1] yes\n[2] not\n[3] and\n[4] or\n[5] nand\n[6] nor\n[7] xor\n[8] xnor\n[q] quit\nyour choice: ")
        if secondInput.isnumeric() and 1 <= int(secondInput) <= 8:
            num = secondInput
            mode2Mode = options2[secondInput]
            second = userInputs(num, mode2Mode)
        elif secondInput == "q":
            print(f'{colors["blue"]}Have a good day{colors["reset"]}')
            return
        else:
            print(f'{colors["red"]}wrong input, try again{colors["reset"]}')
            return

        result = modes.addition(first, second)
        print(f'{colors["green"]}In {mode} mode, the {options2[firstInput]} and {options2[secondInput]} have resulted in {result}{colors["reset"]}')

def userInputs(choice, mode):
    if choice == "1" or choice == "2":
        print(f'{colors["yellow"]}Mode selected: {mode}{colors["reset"]}')
        if choice == "1":
            value = correctInput(choice)
            newValue = truthTables.yesFunction(value)
            print(f'{colors["green"]}In {mode} mode, the value {value} became {newValue}{colors["reset"]}')
            return newValue
        else:
            value = correctInput(choice)
            newValue = truthTables.notFunction(value)
            print(f'{colors["green"]}In {mode} mode, the value {value} became {newValue}{colors["reset"]}')
            return newValue
    else:
        print(f'{colors["yellow"]}Mode selected: {mode}{colors["reset"]}')
        if choice == "3":
            values = correctInput(choice)
            value1 = values[0]
            value2 = values[1]
            newValue = truthTables.andFunction(value1, value2)
            print(f'{colors["green"]}In {mode} mode, the values {value1} and {value2} resulted in {newValue}{colors["reset"]}')
            return newValue
        elif choice == "4":
            values = correctInput(choice)
            value1 = values[0]
            value2 = values[1]
            newValue = truthTables.orFunction(value1, value2)
            print(f'{colors["green"]}In {mode} mode, the values {value1} and {value2} resulted in {newValue}{colors["reset"]}')
            return newValue
        elif choice == "5":
            values = correctInput(choice)
            value1 = values[0]
            value2 = values[1]
            newValue = truthTables.nandFunction(value1, value2)
            print(f'{colors["green"]}In {mode} mode, the values {value1} and {value2} resulted in {newValue}{colors["reset"]}')
            return newValue
        elif choice == "6":
            values = correctInput(choice)
            value1 = values[0]
            value2 = values[1]
            newValue = truthTables.norFunction(value1, value2)
            print(f'{colors["green"]}In {mode} mode, the values {value1} and {value2} resulted in {newValue}{colors["reset"]}')
            return newValue
        elif choice == "7":
            values = correctInput(choice)
            value1 = values[0]
            value2 = values[1]
            newValue = truthTables.xorFunction(value1, value2)
            print(f'{colors["green"]}In {mode} mode, the values {value1} and {value2} resulted in {newValue}{colors["reset"]}')
            return newValue
        else:
            values = correctInput(choice)
            value1 = values[0]
            value2 = values[1]
            newValue = truthTables.xnorFunction(value1, value2)
            print(f'{colors["green"]}In {mode} mode, the values {value1} and {value2} resulted in {newValue}{colors["reset"]}')
            return newValue

while True:
    userchoice1 = input("What would you like to do?\n[1] print logic gate results\n[2] add or multiply logic gates\n[q] quit\nyour choice: ")
    if userchoice1.isnumeric() and 1 <= int(userchoice1) <= 2:
        if userchoice1 == "1":
            userchoice2 = input("which truth table would you want to check?\n[1] yes\n[2] not\n[3] and\n[4] or\n[5] nand\n[6] nor\n[7] xor\n[8] xnor\n[q] quit\nyour choice: ")
            if userchoice2.isnumeric() and 1 <= int(userchoice2) <= 8:
                num = userchoice2
                mode = options2[userchoice2]
                userInputs(num, mode)
            elif userchoice2 == "q":
                print(f'{colors["blue"]}Have a good day{colors["reset"]}')
                break
            else:
                print(f'{colors["red"]}wrong input, try again{colors["reset"]}')
        else:
            option2Mode = input("What would you like to do?\n[1] add\n[2] multiply\n[q] quit\nyour choice: ")
            if option2Mode.isnumeric() and 1 <= int(option2Mode) <= 2:
                user_choice = option2Mode
                mode = options3[option2Mode]
                addOrMultiplyFunction(user_choice, mode)
            elif option2Mode == "q":
                print(f'{colors["blue"]}Have a good day{colors["reset"]}')
                break
            else:
                print(f'{colors["red"]}wrong input, try again{colors["reset"]}')
    elif userchoice1 == "q":
        print(f'{colors["blue"]}Have a good day{colors["reset"]}')
        break
    else:
        print(f'{colors["red"]}wrong input, try again{colors["reset"]}')
