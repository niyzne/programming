import logicGates
import modes
import colors

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

operations = {
    "1": modes.addition,
    "2": modes.multiplication,
}

gates = {
    "1": logicGates.yesFunction,
    "2": logicGates.notFunction,
    "3": logicGates.andFunction,
    "4": logicGates.orFunction,
    "5": logicGates.nandFunction,
    "6": logicGates.norFunction,
    "7": logicGates.xorFunction,
    "8": logicGates.xnorFunction
}

def invalidInput():
    print(f'{colors.colors["red"]}Invalid input, try again{colors.colors["reset"]}')

def goodbye():
    print(f'{colors.colors["blue"]}Have a good day{colors.colors["reset"]}')

def correctInput(choice):
    if choice == "1" or choice == "2":
        while True:
            value = input("Input 1 or 0: ")
            if value.isnumeric():
                value = int(value)
                if (value == 0 or value == 1):
                    break
            invalidInput()
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
            invalidInput()
        return value1, value2

def addOrMultiplyFunction(user_choice, mode):
    print(f'{colors.colors["yellow"]}Mode selected: {mode}{colors.colors["reset"]}')
    results = []
    selectedGates = []

    for i in range(2):
        if i == 0:
            title = "first"
        else:
            title = "second"
        userInput = input(f"For {mode}, what's the {title} operator we will perform?\n[1] yes\n[2] not\n[3] and\n[4] or\n[5] nand\n[6] nor\n[7] xor\n[8] xnor\n[q] quit\nyour choice: ")
        if userInput.isnumeric() and 1 <= int(userInput) <= 8:
            num = userInput
            mode1Mode = options2[userInput]
            selectedGates.append(userInput)
            results.append(userInputs(num, mode1Mode))
        elif userInput == "q":
            goodbye()
            return
        else:
            invalidInput()
            return

    gate = operations[user_choice]
    result = gate(results[0], results[1])
    print(f'{colors.colors["green"]}In {mode} mode, the {options2[selectedGates[0]]} and {options2[selectedGates[1]]} have resulted in {result}{colors.colors["reset"]}')

def userInputs(choice, mode):
    print(f'{colors.colors["yellow"]}Mode selected: {mode}{colors.colors["reset"]}')
    gate = gates[choice]
    if choice == "1" or choice == "2":
        value = correctInput(choice)
        newValue = gate(value)
        print(f'{colors.colors["green"]}In {mode} mode, the value {value} became {newValue}{colors.colors["reset"]}')
        return newValue
    values = correctInput(choice)
    value1 = values[0]
    value2 = values[1]
    newValue = gate(value1, value2)
    print(f'{colors.colors["green"]}In {mode} mode, the values {value1} and {value2} resulted in {newValue}{colors.colors["reset"]}')
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
                goodbye()
                break
            else:
                invalidInput()
        else:
            option2Mode = input("What would you like to do?\n[1] add\n[2] multiply\n[q] quit\nyour choice: ")
            if option2Mode.isnumeric() and 1 <= int(option2Mode) <= 2:
                user_choice = option2Mode
                mode = options3[option2Mode]
                addOrMultiplyFunction(user_choice, mode)
            elif option2Mode == "q":
                goodbye()
                break
            else:
                invalidInput()
    elif userchoice1 == "q":
        goodbye()
        break
    else:
        invalidInput()
