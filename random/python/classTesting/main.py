import classTest

colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "reset": "\033[0m"
}

def randomMessages(computer):
    print(f'{colors["green"]}Computer name: {computer.name}{colors["reset"]}')
    print(f'{colors["green"]}Computer price: {computer.price}{colors["reset"]}')
    print(f'{colors["green"]}Computer company: {computer.company}{colors["reset"]}')
    print(f'{colors["green"]}{computer.nameMessage()}{colors["reset"]}')
    print(f'{colors["green"]}{computer.priceMessage()}{colors["reset"]}')
    print(f'{colors["green"]}{computer.companyMessage()}{colors["reset"]}')

def callComputer():
    print(f'{colors["yellow"]}You\'ve selected to make a computer{colors["reset"]}')
    computerName = input("Input computer name: ")
    while True:
        computerPrice = input("Input computer price: ")
        if computerPrice.isnumeric():
            computerPrice = int(computerPrice)
            break
        print(f'{colors["red"]}Invalid input, try again{colors["reset"]}')
    computerCompany = input("Input computer Company name: ")
    myComputer = classTest.computers(
        computerName, computerPrice, computerCompany
    )
    randomMessages(myComputer)

while True:
    userChoice = input("What do you want to do?\n[1] Make Computer\n[q] quit\nYour Choice: ")
    if userChoice == "1":
        callComputer()
    elif userChoice == "q":
        print(f'{colors["blue"]}Have a good one!{colors["reset"]}')
        break
    else:
        print(f'{colors["red"]}Incorrect statement, try again{colors["reset"]}')
